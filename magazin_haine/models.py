from django.db import models
import uuid
from django.contrib import admin
from django.urls import reverse 
# Create your models here.

class Locatie(models.Model):
    adresa = models.CharField(max_length=255)
    oras = models.CharField(max_length=100)
    judet = models.CharField(max_length=100)
    cod_postal = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.adresa}, {self.oras}"


class Categorie(models.Model):
    id_categorie = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nume = models.CharField(max_length=200)
    descriere = models.TextField()
    imagine_categorie = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.nume
    
    def get_absolute_url(self):
        return reverse('detalii_categorie', kwargs={'nume_categorie': self.nume}) 

class Brand(models.Model):
    id_brand = models.UUIDField(default = uuid.uuid4, editable=False, unique=True)
    nume = models.CharField(max_length=400)
    tara_origine = models.CharField(max_length=200)
    website = models.URLField(blank = True)
    logo = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.nume
    

class Material(models.Model):
    id_material = models.UUIDField(default = uuid.uuid4, editable = False, unique = True)
    nume = models.CharField(max_length=50)
    eco = models.BooleanField(default=True)
    descriere = models.TextField()
    
    def __str__(self):
        return self.nume
    


class Produs(models.Model):
    id_produs = models.UUIDField(default = uuid.uuid4, editable = False, unique = True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="produse")
    nume = models.CharField(max_length=100)
    descriere = models.TextField()
    pret = models.FloatField()
    in_stoc = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="produse_brand")
    materiale = models.ManyToManyField(Material)
    data_adaugare = models.DateField(auto_now_add=True)
    imagine = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.id_produs}, {self.nume}, {self.pret}"
    
    def get_absolute_url(self):
        return reverse('detalii', kwargs={'id_produs': self.id_produs}) 

        

class VariantaProdus(models.Model):
    TIPURI_CULORI = (
        ('albastru', 'albastru'),
        ('alb', 'alb'),
        ('negru', 'negru'),
        ('rosu', 'rosu'),
        ('galben', 'galben'),
        ('roz', 'roz'),
        ('gri', 'gri'),
        ('maro', 'maro'),
    )
    id_varianta = models.UUIDField(default= uuid.uuid4, editable= False, unique = True)
    produs = models.ForeignKey(Produs, on_delete= models.CASCADE, related_name="variante")
    culoare = models.CharField(max_length=10, choices=TIPURI_CULORI)
    marime = models.CharField(max_length=3)
    stoc = models.IntegerField()
    imagine_varianta = models.ImageField(upload_to='produse/',blank=True, null=True)
    
    def __str__(self):
        return f"{self.id_varianta}, {self.marime}, {self.stoc}"
    
class Colectie(models.Model):
    SEZOANE = (
        ('p-v', 'primavara-vara'),
        ('t-i', 'toamna-iarna'),
        ('i', 'iarna'),
        ('p', 'primavara'),
        ('v', 'vara'),
        ('t', 'toamna'),
    )
    id_colectie = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nume = models.CharField(max_length=100)
    sezon = models.CharField(max_length=100, choices=SEZOANE)
    an = models.IntegerField()
    produs = models.ManyToManyField(Produs)
    
    def __str__(self):
        return f"{self.id_colectie}, {self.nume}, {self.sezon}"
    
class Contact(models.Model):
    tipuri_selectare = [
        ('', 'neselectat'),
        ('reclamatie', 'reclamatie'),
        ('intrebare', 'intrebare'),
        ('review', 'review'),
        ('cerere', 'cerere'),
        ('programare', 'programare')
    ]
    nume = models.CharField(max_length=10)
    prenume = models.CharField(max_length=10)
    cnp = models.CharField(max_length=13)
    email = models.EmailField()
    tip_mesaj = models.CharField(max_length=20, choices=tipuri_selectare)
    subiect = models.CharField(max_length=100)
    mesaj = models.TextField()
    varsta = models.CharField(max_length=20)  # ex: "34 ani și 8 luni"
    min_zile = models.PositiveIntegerField()
    urgent = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.nume} - {self.tip_mesaj}'
    
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    tipuri_user = [
        ('bronze' , 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
        ('platinum', 'Platinum')
    ]

    id_user = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)

    nume = models.CharField(max_length=150, blank=False) 
    prenume = models.CharField(max_length=150, blank=False, null = True)
    data_nastere = models.DateField(blank=False, null=True) 
    tip_user = models.CharField(max_length=10, choices=tipuri_user, default='bronze')
    nr_comenzi = models.IntegerField(default=0) 
    tara = models.CharField(max_length=100)
    judet = models.CharField(max_length=100)
    
    # pt email
    email = models.EmailField(unique=False, blank=False)
    cod = models.CharField(max_length=100, blank=True, null=True, unique=True)
    email_confirmat = models.BooleanField(default=False)
    
    telefon = models.CharField(max_length=20, blank=True) 


    #lab 8 task 4
    blocat = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
    class Meta:
        permissions = [
            ("vizualizeaza_oferta", "Poate vedea oferta speciala"),
        ]
    
class Comanda(models.Model):
    metode = [
        ('ramburs', 'ramburs'),
        ('card', 'card')
    ]
    
    id_comanda = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE, related_name="utilizatori")
    produs = models.ManyToManyField(VariantaProdus)
    data = models.DateField(auto_now_add=True)
    pret = models.FloatField(default=0)
    metoda_plata = models.CharField(max_length=10, choices=metode)
    
    def __str__(self):
        return self.id_comanda

MAX_VIEWS = 5

class Vizualizare(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='vizualizari_utilizatori')
    produs = models.ForeignKey(Produs, on_delete=models.CASCADE, related_name='vizualizari_produse')
    data_vizualizare = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} - {self.produs} - {self.data_vizualizare}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        vizualizari = Vizualizare.objects.filter(user=self.user).order_by('data_vizualizare')
        
        if vizualizari.count() > MAX_VIEWS :
            viz_for_delete = vizualizari[: vizualizari.count() - MAX_VIEWS]
            
            for viz in viz_for_delete:
                viz.delete()
        
        
class Promotie(models.Model):
    nume = models.CharField(max_length=50, blank=True)
    data_creare = models.DateField(auto_now_add=True)
    data_expirare = models.DateField()
    
    activ = models.BooleanField(default=True)    
    procent_reducere = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    
    categorii_valabile = models.ManyToManyField(Categorie, related_name='promotii_asociate')
    
    def __str__(self):
        return self.nume
    
    
