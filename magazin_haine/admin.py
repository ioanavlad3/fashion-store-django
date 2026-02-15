from django.contrib import admin
from .models import Locatie
# Register your models here.

from .models import Categorie
from .models import Brand
from .models import Material
from .models import Produs
from .models import VariantaProdus
from .models import Colectie
from .models import Vizualizare
from .models import Promotie
from .models import CustomUser
from .models import Comanda

#admin.site.register(Locatie)

class LocatieAdmin(admin.ModelAdmin):
    list_display = ('adresa', 'oras', 'judet', 'cod_postal')  # afișează câmpurile în lista de obiecte
    list_filter = ('judet', 'oras')  # adaugă filtre laterale
    search_fields = ('adresa', 'cod_postal')  # permite căutarea după anumite câmpuri
    fieldsets = (
        ('Informații Generale', {
            'fields': ('judet', 'oras')
        }),
        ('Date Publicare', {
            'fields': ('adresa', 'cod_postal'),
            'classes': ('collapse',),  # secțiune pliabilă
        }),
    )

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nume', 'descriere')
    search_fields = ('nume', 'descriere')
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ('nume', 'tara_origine', 'website')
    search_fields = ('nume', 'tara_origine')
    
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nume', 'eco', 'descriere')
    search_fields = ('nume', 'eco')
    
#ordine schimbata
#crescator dupa pret
class ProdusAdmin(admin.ModelAdmin):
    list_display = ('nume', 'categorie', 'descriere', 'pret', 'in_stoc', 'brand', 'data_adaugare', 'imagine')
    search_fields = ('nume', 'brand')
    ordering = ('pret',)  
    list_per_page = 5
    
    fieldsets = (
        ('Informatii esentiale', {
            'fields': ('nume', 'pret', 'in_stoc', 'brand', 'categorie', 'imagine')
        }),

        ('Detalii optionale', {
            'fields': ('descriere', 'materiale'),
            'classes': ('collapse',),  
        }),
    )
    

    
class VariantaProdusAdmin(admin.ModelAdmin):
    list_display = ('culoare', 'marime', 'stoc')
    search_fields = ('culoare', 'marime')
    
class ColectieAdmin(admin.ModelAdmin):
    list_display = ('nume', 'an', 'sezon')
    search_fields = ('nume', 'sezon')
    list_filter = ('an', 'sezon') 

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'nume', 'prenume', 'data_nastere', 'tip_user', 'nr_comenzi', 'tara', 'judet', 
                    'email', 'cod', 'telefon')


class ComandaAdmin(admin.ModelAdmin):
    list_display = ('id_comanda', 'user', 'data', 'pret')

admin.site.register(Locatie, LocatieAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Produs, ProdusAdmin)
admin.site.register(VariantaProdus, VariantaProdusAdmin)
admin.site.register(Colectie, ColectieAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Comanda, ComandaAdmin)

admin.site.site_title = "Administrare Magazin"
admin.site.site_header = "Aurora Boutique - Panou Administrare"
admin.site.index_title = "Bun venit in zona de administrare"
