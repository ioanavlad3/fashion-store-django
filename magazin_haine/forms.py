from django import forms
import string
tipuri_selectare = [
    ('', 'neselectat'),
    ('reclamatie', 'reclamatie'),
    ('intrebare', 'intrebare'),
    ('review', 'review'),
    ('cerere', 'cerere'),
    ('programare', 'programare')
]
from datetime import date
from django import forms
from datetime import date
from.models import Contact

def onlyLettersAndSpaces(value):
    if not value:
        return
    if not value[0].isupper():
        raise forms.ValidationError("Trebuie sa inceapa cu litera mare.")
    for c in value:
        if not (c.isalpha() or c in [' ', '-']):
            raise forms.ValidationError("Sunt permise doar litere, spatii si cratime.")

def firstLetterUpper(value):
    if not value:
        return
    for i in range(len(value)):
        if value[i] in [' ', '-']:
            if i + 1 < len(value) and not value[i + 1].isupper():
                raise forms.ValidationError("Fiecare cuvânt trebuie să aibă inițială mare.")


class ContactForm(forms.ModelForm):
    data_nastere = forms.DateField(label = 'Data nastere:', required = True, widget=forms.DateInput(attrs={'type': 'date'}))
    confirmare_email = forms.EmailField(label = 'Confirmare Email')

    class Meta:
        model = Contact
        fields = ['nume','prenume','cnp','email','data_nastere',
            'tip_mesaj','subiect','mesaj','min_zile']
        
        
    def clean_nume(self):
        nume = self.cleaned_data.get('nume')
        
        try:
            onlyLettersAndSpaces(nume)
            firstLetterUpper(nume)
        except forms.ValidationError as e:
            raise e
            
        return nume
    
    def clean_prenume(self):
        prenume = self.cleaned_data.get('prenume')
        
        try:
            validator_litera_mica(prenume)
            firstLetterUpper(prenume)
        except forms.ValidationError as e:
            raise e
            
        return prenume
        
        
    def clean_subiect(self):
        subiect = self.cleaned_data.get('subiect')
        
        try:
            validator_litera_mica(subiect)
            firstLetterUpper(subiect)
        except forms.ValidationError as e:
            raise e
            
        return subiect
        
    
    def clean_cnp(self):
        cnp = self.cleaned_data.get('cnp')
        if not cnp:
            return cnp
        if not cnp.isdigit():
            raise forms.ValidationError("CNP-ul trebuie să conțină doar cifre.")
        if cnp[0] not in ['1', '2']:
            raise forms.ValidationError("Trebuie să înceapă cu 1 sau 2.")
        an = int(cnp[1:3])
        luna = int(cnp[3:5])
        zi = int(cnp[5:7])
        try:
            date(1900 + an, luna, zi)
        except:
            raise forms.ValidationError("CNP invalid.")
        return cnp

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'guerillamail.com' in email or 'yopmail.com' in email:
            raise forms.ValidationError('Email-ul este temporar!')
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirmare_email")
        if email and confirm_email and email != confirm_email:
            raise forms.ValidationError("Adresele de email nu coincid.")

        data_nastere = cleaned_data.get('data_nastere')
        if data_nastere:
            azi = date.today()
            varsta = azi.year - data_nastere.year - (
                (azi.month, azi.day) < (data_nastere.month, data_nastere.day)
            )
            if varsta < 18:
                raise forms.ValidationError("Trebuie sa ai minim 18 ani.")
            
        # la finalul mesajului se gaseste numele user ului
        
        nume = self.cleaned_data.get('nume')
        if nume:
            nume = nume.strip()
            
        mesaj = self.cleaned_data.get('mesaj')
        if mesaj:
            mesaj = mesaj.strip()
        
        # if nume and mesaj:
        #     # Ia ultimul cuvânt
        #     last_word = mesaj.split()[-1]
            
        #     # Curăță ultimul cuvânt de semne de punctuație
        #     # Ex: transforma "Gigel." in "Gigel"
        #     last_word_curat = last_word.strip(string.punctuation)
            
        #     if last_word_curat != nume:
        #         # Păstrează eroarea pentru a împiedica salvarea în fișier
        #         raise forms.ValidationError('Mesaj invalid: Ultimul cuvânt din mesaj trebuie să fie identic cu numele.')
            
            
        min_zile = self.cleaned_data.get('min_zile')
        tip = self.cleaned_data.get('tip_mesaj')
        
        if min_zile:
            if min_zile > 30:
                raise forms.ValidationError('Maximul de zile e de 30')        
            if tip in ['review', 'cerere'] and min_zile < 4 :
                    raise forms.ValidationError('Prea putine zile')
                
            if tip in ['cerere', 'intrebare'] and min_zile < 2:
                    raise forms.ValidationError('Prea putine zile')
            
        # cnp -ul corespunde cu data nasterii
        
        cnp = self.cleaned_data.get('cnp')
        
        if cnp and data_nastere:
            an = int(cnp[1:3])
            luna = int(cnp[3:5])
            zi = int(cnp[5:7])
            
            if an != (data_nastere.year % 100) or luna != data_nastere.month or zi != data_nastere.day:
                raise forms.ValidationError('Data nu corespunde cu cnp-ul')
            
        return cleaned_data
        



TIPURI_CULORI = [
    ('', 'Alege o culoare'),
    ('albastru', 'Albastru'),
    ('alb', 'Alb'),
    ('negru', 'Negru'),
    ('rosu', 'Roșu'),
    ('galben', 'Galben'),
    ('roz', 'Roz'),
    ('gri', 'Gri'),
    ('maro', 'Maro'),
]


from .models import Categorie, Brand, Material

TIPURI_CATEGORII = Categorie.objects.all()
TIPURI_BRAND = Brand.objects.all()
TIPURI_MATERIALE = Material.objects.all()

class FiltreProduse(forms.Form):
    #categorie = forms.CharField(max_length=100, label='Categorie', required=False)
    categorie = forms.ModelChoiceField(queryset = TIPURI_CATEGORII, label = "Categorie", required=False)
    brand = forms.ModelChoiceField(queryset = TIPURI_BRAND, label = 'Brand', required=False)
    pret_min = forms.IntegerField(label = 'Pret minim', required=False)
    pret_max = forms.IntegerField(label = 'Pret maxim', required=False)
    culoare = forms.ChoiceField(choices=TIPURI_CULORI, label='Culoare', required=False)
    marime = forms.CharField(label='Marime', required=False)
    in_stoc = forms.BooleanField(label='In stoc', required=False, initial=False,)
    eco = forms.BooleanField(label = 'eco', required=False, initial=False)
    elem_pag = forms.IntegerField(label = 'Elemente pe pagina', required=False)
    materiale = forms.ModelMultipleChoiceField(queryset = TIPURI_MATERIALE, label = 'Materiale', required = False)
    
    def clean_pret_min(self):
        pret_min = self.cleaned_data.get("pret_min")
        if pret_min and pret_min < 0:
            raise forms.ValidationError("Pretul minim nu poate fi negativ.")
        return pret_min

    def clean_pret_max(self):
        pret_max = self.cleaned_data.get("pret_max")
        if pret_max and pret_max < 0:
            raise forms.ValidationError("Pretul maxim nu poate fi negativ.")
        return pret_max

    def clean_marime(self):
        marime = self.cleaned_data.get("marime")
        if marime and len(marime) > 3:
            raise forms.ValidationError("Marimea trebuie sa aiba maximum 3 caractere.")
        return marime

    def clean(self):
        cleaned_data = super().clean()
        pret_min = cleaned_data.get("pret_min")
        pret_max = cleaned_data.get("pret_max")

        if pret_min and pret_max :
            if pret_min > pret_max:
                raise forms.ValidationError(
                    "Pretul minim nu poate fi mai mare decat pretul maxim."
                )
    
from .models import Produs

def validator_pozitiv(val):
    if val < 0:
        raise forms.ValidationError('Valoarea trebuie sa fie > 0')
    
def validator_lg_minima(val):
    if len(val) < 10:
        raise forms.ValidationError("Trebuie sa introduci minim 10 caractere")
    
def validator_par(val):
    if val % 2 != 0:
        raise forms.ValidationError('Trebuie un numar par')
    
def validator_litera_mica(s):
    if s[0].islower():
        raise forms.ValidationError('Trebuie sa inceapa cu litera mare')

class ProdusForm(forms.ModelForm):
    pret_baza = forms.FloatField(label='Pret de baza', required=True,
                            validators=[validator_pozitiv, validator_par],
                            help_text = 'Introdu pretul de baza: un numar par')
    
    adaos = forms.FloatField(label='Adaos (%)', required=True,
                            validators=[validator_pozitiv],
                            help_text="Marja de profit.(intre 10 si 50 %)")
    
    

    class Meta:
        model = Produs
        fields = ['brand', 'nume', 'descriere', 'in_stoc', 'materiale', 'imagine', 'categorie']
        labels = {'nume' : 'Numele Produsului',
                    'descriere' :"Descrierea Produsului"}
        widgets = {
            'materiale': forms.CheckboxSelectMultiple(),
        }
        

    def save(self, commit=True):
        obj = super().save(commit=False)

        pret_baza = self.cleaned_data.get('pret_baza')
        adaos = self.cleaned_data.get('adaos')
        descriere = self.cleaned_data.get('descriere')

        # calculam pret final si categorie
        obj.pret = pret_baza + pret_baza * (adaos / 100)
        # # numele e de forma :tricou + id
        # categorie = self.cleaned_data.get('categorie')
        # id_produs = self.cleaned_data.get('id_produs')
        
        # obj.nume = f'{categorie}{id_produs}'
        

        if commit:
            obj.save()
        return obj

    def clean_nume(self):
        nume = self.cleaned_data.get('nume')

        try:
            validator_litera_mica(nume)
        except forms.ValidationError as e:
            raise e
            
        return nume
        
    def clean_descriere(self):
        descriere = self.cleaned_data.get('descriere')
        
        try:
            validator_lg_minima(descriere)
            validator_litera_mica(descriere) 
        except forms.ValidationError as e:
            raise e
            
        return descriere

    
    def clean(self):
        cleaned_data = super().clean()
        
        descriere = self.cleaned_data.get('descriere')
        categorie = self.cleaned_data.get('categorie')
        if descriere:
            descriere_cuv = descriere.split()
            if descriere_cuv[0] != categorie:
                raise forms.ValidationError('Descrierea trebuie sa se potriveasca cu categoria')
        
        
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    nume = forms.CharField(max_length=150, label = 'Nume')
    prenume = forms.CharField(max_length=150, label = 'Prenume')
    
    data_nastere = forms.DateField(
        label = 'Data nasterii:',
        widget = forms.DateInput(attrs = {'type' : 'date'}),
        required=True
    )
    
    telefon = forms.CharField(max_length=20, required=True, label = 'Numar de telefon:')
    
    class Meta:
        model = CustomUser
        
        fields = ('username', 'email', 'nume', 'prenume', 'data_nastere', 'telefon', 'tara', 'judet')
        
    def clean_data_nastere(self):
        data_nastere = self.cleaned_data.get('data_nastere')
        
        if data_nastere:
            ani = date.today().year - data_nastere.year
            
            luni = date.today().month - data_nastere.month
            if luni < 0:
                luni += 12
                ani -= 1
            
            if ani < 18:
                raise forms.ValidationError("Trebuie sa ai minim 18 ani.")
            
            return data_nastere
            
    def clean_telefon(self):
        telefon = self.cleaned_data.get('telefon')
        if telefon:
            if telefon[:3] != '+40':
                raise forms.ValidationError('Prefixul de Romania est +40')
            
        return telefon
    
    def clean_nume(self):
        nume = self.cleaned_data.get('nume')
        try:
            onlyLettersAndSpaces(nume)
        except forms.ValidationError as e:
            raise e
            
        return nume
        
    def save(self, commit=True):
        user = super().save(commit=False)
        
        user.nume = self.cleaned_data["nume"]
        user.data_nastere = self.cleaned_data["data_nastere"]
        user.telefon = self.cleaned_data["telefon"]
        
        if commit:
            user.save()
        return user
            
            
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    # camp de tip boolean (checkbox) pentru optiunea "Tine-ma minte"
    remember_me = forms.BooleanField(required=False, initial=False, label="Tine-ma minte pe acest dispozitiv (24 ore)")
    
    def clean(self):
        cleaned_data = super().clean() 
        return cleaned_data



from .models import Promotie
from django.forms import Textarea

class PromotieForm(forms.ModelForm):
    subiect = forms.CharField(max_length=200, required=False)
    mesaj = forms.CharField(widget=forms.Textarea, required=False)
    minim_accesari = forms.IntegerField(required=False)
    # timp_promotie = forms.DateTimeField(required=False)
    
    categorii_valabile = forms.ModelMultipleChoiceField(
        queryset=Categorie.objects.all(),   
        label="Categorie",
        required=False
    )

    class Meta:
        model = Promotie
        fields = ['nume', 'data_expirare', 'procent_reducere', 'activ']
        widgets = {
            'data_expirare': forms.DateInput(attrs={'type': 'date'})
        }

    def save(self, commit=True):
        promotie = super().save(commit=False)

        if commit:
            promotie.save()
            self.save_m2m()

        return promotie
