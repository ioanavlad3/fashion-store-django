from django.shortcuts import render, redirect
from datetime import datetime

from . import middleware as mw
from collections import Counter
# Create your views here.

from django.http import HttpResponse, HttpResponseForbidden

from django.core.paginator import Paginator
from .models import Produs
from .models import VariantaProdus

from .models import Locatie
from .models import CustomUser

from django.contrib.auth.decorators import permission_required

import logging

logger = logging.getLogger('django')

def index(request):
	return HttpResponse("""
                        <html>
                        <body>
                        <h1>Informatii despre server</h1>
                        </body>
                        </html>
                        """)

def colectii(request):
    return render(request, 'magazin_haine/colectii.html')

def brands(request):
    return render(request, 'magazin_haine/branduri.html')

def info(request):
    # daca nu face parte din grup, atunci nu poate accesa pagina
    if not request.user.groups.filter(name='Administratori_site').exists():
        return render(request, interzis,
                        titlu='Eroare la pagina de info',
                        mesaj_personalizat='Nu ai dreptul sa intri pe aceasta pagina')
    else:
        return HttpResponse(f"""
                            <html>
                            <body>
                            <h1>Informatii despre server</h1>
                            <p>{request.GET.get("a")}</p>
                            <p>{request.GET.getlist("a")}</p>
                            </body>
                            </html>
                            """)
    


def afis_template(request):
    return render(request,"magazin_haine/exemplu.html",
        {
            "titlu_tab":"Titlu fereastra",
            "titlu_articol":"Titlu afisat",
            "continut_articol":"Continut text"
        }
    )
    
def afis_template2(request):
    return render(request, "magazin_haine/simplu.html")


days = ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica"]
months = ["Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie",
        "Iulie", "August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie"]

def afis_data(param):
    now = datetime.now()
    
    section = "<h2>Data si ora</h2>"

    data_f = f"{days[now.weekday()]}, {now.day} {months[now.month-1]} {now.year}"
    hour_f = now.strftime("%H:%M:%S")

    if param == "zi":
        section += f"<p>{data_f}</p>"
    elif param == "timp":
        section += f"<p>{hour_f}</p>"
    else:
        section += f"<p>{data_f} {hour_f}</p>"

    return section


def afisare(request):
    param = request.GET.get("data")   
    continut = """
        <html>
        <body>
        <h1>Informatii despre server</h1>
    """

    if param:
        continut += afis_data(param)

    continut += """
        </body>
        </html>
    """
    return HttpResponse(continut)

from urllib.parse import urlparse, parse_qs

class Accesare:
    _counter = 0
    
    def __init__(self, ip_client, url):
        Accesare._counter += 1
        self.id = Accesare._counter
        self.ip_client = ip_client
        self.url = url
        self.data = datetime.now()
    
    
    def lista_parametri(self):
        parsed = urlparse(self.url)
        params = parse_qs(parsed.query)
        L = []
        
        for key, value in params.items():
            if value:
                L.append((key, value))
            else:
                L.append((key, None))

        return L
    
    def url(self):
        return self.url

    def data(self, formatare_str):
        return self.data.strftime(formatare_str)     

    def pagina(self):
        parsed = urlparse(self.url)
        return parsed.path
    





def log(request):
    if not request.user.groups.filter(name='Administratori_site').exists():
        return render(request, interzis,
                        titlu='Eroare la pagina log',
                        mesaj_personalizat='Nu ai dreptul sa intri pe aceasta pagina')
    
    logs = list(mw.REQUEST_LOG)
    errors = []

    accesari_val = (request.GET.get("accesari") or "").strip().lower()
    nr_accesari = (accesari_val == "nr")
    details = (accesari_val == "detalii")
    total_count  = mw.COUNT

    # iduri
    #["2,3", "5", "4,2,1"]
    raw_iduri = request.GET.getlist("iduri")  
    wanted_ids = []
    for id in raw_iduri:
        for tok in id.split(","):
            tok = tok.strip()
            if tok == "": 
                continue
            if tok.isdigit():
                wanted_ids.append(int(tok)) # adauga la lista
        

    # dubluri
    val = request.GET.get("dubluri", "false").lower()
    if val in {"true", "yes"}:
        allow_dups = True
    else:
        allow_dups = False
        
    show_ids = bool(wanted_ids) 


    if wanted_ids:
        by_id = {item["id"]: item for item in logs}
        ordered = []
        seen = set()
        for i in wanted_ids:
            if i in by_id:
                # ID cerut exista in dict
                if allow_dups or i not in seen:
                    ordered.append(by_id[i])
                seen.add(i)
            else:
                errors.append(f"Accesarea cu id {i} nu mai exista")
        logs = ordered
    else:
        # daca nu s-au cerut ID-uri, se cer 'ultimele'
        last = request.GET.get("ultimele")
        if last is not None:
            n = int(last)
            total = len(logs)
            if n < total:
                logs = logs[-n:]  # ultimele n
            elif n > total:
                errors.append(f"sunt doar {total} accesari fata de {n} accesari cerute.")
            

    # cati parametri a primit si numele acestora
    nr_parametri = len(request.GET)
    nume_parametri = list(request.GET.keys())
    
    # lista completa a campurilor disponibile
    ALL_FIELDS = ["id", "path", "data"]
    # etichete pentru coloane
    LABELS = {"id": "ID", "path": "cale", "data": "data"}


    tabel_raw = request.GET.get("tabel")
    table_columns = None  

    # procesare tabel
    if tabel_raw:
        val = tabel_raw.strip().lower()
        if val == "tot":
            table_columns = ALL_FIELDS[:]  # toate coloanele
        else:
            cols = []
            # split la fiecare virgula
            for part in val.split(","):
                name = part.strip().lower()
                if name in ALL_FIELDS and name not in cols:
                    cols.append(name)
                else:
                    if name not in ALL_FIELDS:
                        errors.append(f"Coloana invalida: {part.strip()}")
            if cols:
                table_columns = cols
            

        # sincronizeaza cu show_ids
        if table_columns is not None:
            show_ids = show_ids or ("id" in table_columns)
        
    # construiesc lista de coloane pentru template
        
    display_cols = None
    
    if tabel_raw:
        if table_columns: 
            display_cols = [{"key": k, "label": LABELS[k]} for k in table_columns]
        else:
            display_cols = []  
            
    # statistici suplimentare  
    path_counter = Counter(item["path"] for item in mw.REQUEST_LOG)
    if path_counter:
        most_common_path, most_common_count = path_counter.most_common(1)[0]
        least_common_path, least_common_count = path_counter.most_common()[-1]

    return render(request, "magazin_haine/log.html", {
        "logs": logs,
        "errors": errors,
        "show_count": nr_accesari,
        "total_count": total_count,
        "show_ids": show_ids,
        "show_details": details,
        "num_parametri": nr_parametri,
        "nume_parametri": nume_parametri,
        "table_columns": table_columns,
        "display_cols": display_cols,
        "TABLE_LABELS": LABELS,
        "most_common_path": most_common_path,
        "most_common_count": most_common_count,
        "least_common_path": least_common_path,
        "least_common_count": least_common_count,
        "months" : months,
    })
    

def afis_loc(request):
    locatii = Locatie.objects.all()
    return render(request, "magazin_haine/locatie.html", {
        'locatii' : locatii,
        # 'prima_locatie' : locatii[0],
        'nr_locatii' : len(locatii),
        
    })
    
    

def despre(request):
    return render(request, "magazin_haine/despre.html", )


def in_lucru(request):
    return render(request, "magazin_haine/in_lucru.html", )

def cont(request):
    return render(request, 'magazin_haine/cont.html', )

def error_404_view(request, exception):
    return render(request, 'in_lucru.html', status=404, )

# def get_ip(request):
#     # IP-ul este deja în request.client_ip
#     ip = getattr(request, 'client_ip', 'Necunoscut')
#     return render(request, 'magazin_haine/baza.html', {'ip': ip})

def get_ip(request):
    # daca adresa e in spatele unui proxy
    str_lista_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if str_lista_ip:
        return str_lista_ip.split(',')[0].strip()
    # daca e conectat direct la server
    else:
        return request.META.get('REMOTE_ADDR')
    
def baza(request):
    return render(request, 'magazin_haine/baza.html')
    
def principala(request):
    return render(request, "magazin_haine/principal.html", {'ip': get_ip(request)})

def lista_produse(request):
    fel_sort = request.GET.get('sort')

    if fel_sort == 'a':
        produse = Produs.objects.prefetch_related('variante').order_by('nume')
    else:
        produse = Produs.objects.prefetch_related('variante').order_by('-nume')

    paginator = Paginator(produse, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'magazin_haine/lista_produse.html', {
        'page_obj': page_obj,
        'ip': get_ip(request)
    })

from .models import Categorie

def lista_categorii(request):
    categorii = Categorie.objects.all()
    paginator = Paginator(categorii, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'magazin_haine/categorii.html', {
        'page_obj': page_obj,
        'ip': get_ip(request),
    })
    
from .forms import ContactForm
from datetime import date
import os, time, json
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if not form.is_valid():
            print(form.errors) 
        if form.is_valid():  
            # nu salvam datele imediat

            obj = form.save(commit=False)
            
            # salvam varsta in ani si luni
            data_nastere = form.cleaned_data.get('data_nastere')
            today = date.today()
            
            years = today.year - data_nastere.year
            months = today.month - data_nastere.month
            
            if months < 0:
                years -= 1
                months += 12
                
            obj.varsta = f"{years} ani si {months} luni"
            
            # curatare mesaj
            
            mesaj = form.cleaned_data.get('mesaj')
            if mesaj:
                mesaj = mesaj.strip()
                mesaj = mesaj.replace('\n', ' ')

                l = mesaj.split()
                mesaj2 = ' '.join(l)
                mesaj = mesaj2
            
            # dupa [.?!...] =>  litera mare
            
            rezultat = ""
            capitalize_next = True
            for c in mesaj:
                if capitalize_next and c.isalpha():
                    rezultat += c.upper()
                    capitalize_next = False
                else:
                    rezultat += c
                if c in ".?!":
                    capitalize_next = True

            obj.mesaj = rezultat
                    
            # setare urgent
            
            tip = form.cleaned_data.get('tip_mesaj')
            min_zile = form.cleaned_data.get('min_zile')

            if (tip in ['review','cerere'] and min_zile == 4) or \
                (tip in ['cerere','intrebare'] and min_zile == 2):
                obj.urgent = True
            else:
                obj.urgent = False
            
            # salvere
            obj.save()            
            
            # salvare fisier cu nume
            
            # creare folder mesage
            folder_path = os.path.join(settings.BASE_DIR, 'magazin_haine', 'Mesaje')
            os.makedirs(folder_path, exist_ok=True)

            # preluare date din formular
            data = form.cleaned_data.copy()
            data.pop('confirmare_email')  # stergem confirmarea emailului

            # adaugam date suplimentare
            data['ip'] = request.META.get('REMOTE_ADDR')
            # data['data_ora'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data['varsta'] = obj.varsta  # pus anterior in view
            data['urgent'] = obj.urgent

            # creare nume de fisier
            timestamp = int(time.time())
            filename = f"mesaj_{timestamp}"
            if obj.urgent:
                filename += "_urgent"
            filename += ".json"

            file_path = os.path.join(folder_path, filename)

            # scriere in fisier json

            print("Calea completă de salvare:", file_path)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4, default = str)

            # procesarea datelor 
            return redirect('lista_produse')
    else:
        print('nu e ok')
        form = ContactForm()
    return render(request, 'magazin_haine/contact.html', {'form': form, })

from .forms import FiltreProduse
from django.core.paginator import Paginator

def produs_view(request):

    if request.method == "GET":
        form = FiltreProduse(request.GET)
    else:
        form = FiltreProduse()

    fel_sort = request.GET.get('sort')

    variante = VariantaProdus.objects.select_related(
        'produs', 'produs__categorie', 'produs__brand'
    )

    # sortare
    if fel_sort == 'a':
        variante = variante.order_by('produs__nume')
    else:
        variante = variante.order_by('-produs__nume')

    paginare = 10

    if request.method == "GET" and form.is_valid():
        categorie = form.cleaned_data.get('categorie')
        brand = form.cleaned_data.get('brand')
        pret_min = form.cleaned_data.get('pret_min')
        pret_max = form.cleaned_data.get('pret_max')
        culoare = form.cleaned_data.get('culoare')
        marime = form.cleaned_data.get('marime')
        in_stoc = form.cleaned_data.get('in_stoc')
        elem_pag = form.cleaned_data.get('elem_pag')
        materiale = form.cleaned_data.get('materiale')
        eco = form.cleaned_data.get('eco')

        if categorie:
            variante = variante.filter(produs__categorie=categorie)

        if brand:
            variante = variante.filter(produs__brand=brand)

        if pret_min:
            variante = variante.filter(produs__pret__gte=pret_min)

        if pret_max:
            variante = variante.filter(produs__pret__lte=pret_max)

        if culoare:
            variante = variante.filter(culoare=culoare)

        if marime:
            variante = variante.filter(marime__iexact=marime)

        if in_stoc:
            variante = variante.filter(stoc__gt=0)

        if eco:
            variante = variante.filter(produs__materiale__eco=True)

        if materiale:
            variante = variante.filter(produs__materiale__in=materiale)

        if elem_pag:
            paginare = elem_pag

    paginator = Paginator(variante, paginare)
    page_number = request.GET.get('page')
    #extrage efectiv produsele
    page_obj = paginator.get_page(page_number)

    return render(request, 'magazin_haine/lista_produse.html', {
        'filtre': form,
        'page_obj': page_obj,
    })


from django.shortcuts import get_object_or_404
from .models import Vizualizare


def detalii_produs(request, id_produs):
    produs = get_object_or_404(Produs, id_produs = id_produs )
    
    variante = produs.variante.all()
    
    #salvam vizualizarea doar daca user-ul e logat
    if request.user.is_active == True:
        Vizualizare.objects.create(
            user = request.user,
            produs = produs,
        )
    
    
    return render(request,  'magazin_haine/detalii_produs.html', 
                    {
                        'produs':produs,
                        'variante' : variante,
                    })

from django.contrib import messages
from django.http import HttpResponseRedirect


def detalii_categorie(request, nume_categorie):

    # Categoria din URL 
    categorie_selectata = get_object_or_404(Categorie, nume=nume_categorie)

    # Daca userul incearca sa modifice categoria manual, il blocam
    categorie_form = request.GET.get("categorie") or request.POST.get("categorie")
    if categorie_form and str(categorie_form) != str(categorie_selectata.pk):
        messages.error(request, "Nu puteti modifica categoria!")
        return HttpResponseRedirect(request.path)

    # Setare categorie implicita in formular
    initial_data = {"categorie": categorie_selectata.pk}

    # initializez formularul
    if request.method == "GET":
        form = FiltreProduse(request.GET, initial=initial_data)
    else:
        form = FiltreProduse(initial=initial_data)

    # Produse doar din categoria respectiva
    produse = Produs.objects.filter(categorie=categorie_selectata).prefetch_related('variante')

    paginare = 10
    # filtre
    if request.method == "GET" and form.is_valid():

        brand = form.cleaned_data.get("brand")
        pret_min = form.cleaned_data.get("pret_min")
        pret_max = form.cleaned_data.get("pret_max")
        culoare = form.cleaned_data.get("culoare")
        marime = form.cleaned_data.get("marime")
        in_stoc = form.cleaned_data.get("in_stoc")
        elem_pag = form.cleaned_data.get("elem_pag")

        if brand:
            produse = produse.filter(brand__pk=brand.pk)

        if pret_min is not None:
            produse = produse.filter(pret__gte=pret_min)

        if pret_max is not None:
            produse = produse.filter(pret__lte=pret_max)

        if culoare:
            produse = produse.filter(variante__culoare=culoare)

        if marime:
            produse = produse.filter(variante__marime__iexact=marime)

        if in_stoc:
            produse = produse.filter(variante__stoc__gt=0)

        produse = produse.distinct()  

        if elem_pag:
            paginare = elem_pag


    paginator = Paginator(produse, paginare)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, 'magazin_haine/detalii_categorie.html', {
        "produs": categorie_selectata,
        "filtre": form,
        "page_obj": page_obj,
        'ip' : get_ip(request)
    })

from .forms import ProdusForm


def adauga_produse(request):
    if not request.user.has_perm('magazin_haine.add_produs'):
        return HttpResponseForbidden(render(request, 'magazin_haine/403.html', {
            'titlu': 'Eroare pagina',
            'mesaj_personalizat': 'Nu ai voie sa adugi produse'
        }))
    
    if request.method == 'POST':
        form = ProdusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adauga_produse')
    else:
        form = ProdusForm()

    return render(request, 'magazin_haine/adauga_produse.html', {'form': form})

from .forms import CustomUserCreationForm
import random
import string

from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def trimite_mail(user, link_mail):
    context = {'nume': user.nume,
                'user_link' : link_mail}  
    html_content = render_to_string('magazin_haine/template_email.html', context)

    email = EmailMessage(
        subject='Confirmare mail',
        body=html_content,
        from_email='ioionutza.03vlad.gmail.com',
        to=[user.email],
    )
    email.attach_file("C:/Users/ioana/Desktop/Unibuc/Django/magazin/magazin_haine/static/magazin_haine/images/logo.png")
    email.content_subtype = 'html'
    # fail_silently indica daca erorile trebuiesc afisate sau nu 
    email.send(fail_silently=False)
    
    
from django.urls import reverse
from django.core.mail import mail_admins

def inregistrare_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            # daca incearca sa se inregistreze ca 'admin'
            if username.lower() == 'admin':
                mail_admins(
                    subject="cineva incearca sa ne preia site-ul",
                    message=(
                        "Cineva a incercat sa se inregistreze cu username-ul 'admin'.\n"
                        f"Email folosit: {email}"
                    ),
                    html_message=(
                        "<h1 style='color:red;'>Cineva incearca sa se iregistreze ca ADMIN!</h1>"
                        f"<p>Email folosit: {email}</p>"
                    )
                )
                logger.critical('User incearca sa se conecteze cu username nepermis')

                messages.error(request, "Acest username este interzis.")
                return redirect('inregistrare')   # nu se creaza userul

            # pputem crea userul
            user = form.save(commit=False)

            cod_random = ''.join(
                random.choices(string.ascii_uppercase + string.digits, k=100)
            )
            user.cod = cod_random

            user.save()

            #creare link 
            
            url_relativ = reverse('confirma_mail', kwargs={'cod_user': user.cod})
            user_link = f'http://localhost:8000{url_relativ}'

            trimite_mail(user, user_link)

            return redirect('login')

    else:
        form = CustomUserCreationForm()

    return render(request, 'magazin_haine/inregistrare.html', {'form': form})


def confirma_mail(request, cod_user):
    user = get_object_or_404(CustomUser, cod = cod_user)
    
    if not user.email_confirmat:
        user.email_confirmat = True
        user.is_active = True
        user.save()
        messages.success(request, 'Mail confirmat cu succes')
    else:
        messages.info(request, 'Mail-ul a fost deja confirmat')
        
    return render(request, 'magazin_haine/confirma_mail.html', {'user' : user})

from .forms import CustomAuthenticationForm
from django.contrib.auth import authenticate, login, logout

from datetime import datetime


def login_view(request):

    # initializezi lista
    if "loginFail" not in request.session:
        request.session["loginFail"] = []

    
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        # login esuat
        if not form.is_valid():
            messages.debug(request, 'Login esuat')
            attempts = request.session["loginFail"]

            attempts.append({
                "username": request.POST.get("username"),
                "ip": get_ip(request),
                "time": datetime.now().isoformat()   
            })

            request.session["loginFail"] = attempts

            # ultimele 2 minute
            now = datetime.now()
            recent = 0

            for a in attempts:
                t = datetime.fromisoformat(a["time"])
                if (now - t).total_seconds() <= 120:
                    recent += 1

            if recent >= 3:
                mail_admins(
                    subject="Logari suspecte",
                    message=(
                        "Au avut loc 3 incercari de logare esuate in ultimele 2 minute.\n"
                        f"Username: {attempts[-1]['username']}\n"
                        f"IP: {attempts[-1]['ip']}"
                    ),
                    html_message=(f"<h1 style = color : red;>Logari suspecte </h1>" 
                                f"S-au detectat 3 incercari esuate.\n" 
                                f"Username: {attempts[-1]['username']}\n" 
                                f"IP: {attempts[-1]['ip']}"),
                    fail_silently=False
                )
                logger.warning('User care si-a uitat contul detectat')

            # continui cu form invalid
            return render(request, "magazin_haine/login.html", {"form": form})

        # login reusit
        else:

            user = form.get_user()

            if not user.email_confirmat:
                messages.warning(request, "Trebuie sa iti confirmi adresa de email.")
                return redirect("login")

            # reset incercari
            request.session["loginFail"] = []

            login(request, user)

            remember_me = form.cleaned_data.get("remember_me")
            if remember_me: # sesiunea expira la 24 de ore (24 * 60 * 60 secunde) 
                request.session.set_expiry(86400) 
            else: # Daca nu a bifat, sesiunea expira la inchiderea browser-ului 
                request.session.set_expiry(0)

            return redirect("principala")
    else:
        form = CustomAuthenticationForm()

    return render(request, "magazin_haine/login.html", {"form": form})


def logout_view(request):
    
    logout(request)
    return redirect('magazin_haine/login')

from django.contrib.auth.decorators import login_required
from .models import CustomUser
import traceback 

@login_required # Doar utilizatorii autentificati pot accesa
def profil_view(request):
    try:
        user_instance = request.user
        messages.debug(request, f"User ID: {user_instance.id}")
        messages.success(request, 'Datele utilizator sunt furnizate cu succes')
        #  datele relevante din tabela Utilizator
        profile_data = {
            'nume': user_instance.nume,
            'prenume':user_instance.prenume,
            'email': user_instance.email,
            'data_nastere': user_instance.data_nastere.strftime("%Y-%m-%d") if user_instance.data_nastere 
                                                                else 'N/A',
            'tip_user': user_instance.tip_user,
            'nr_comenzi': user_instance.nr_comenzi,
        }
        
        
    except CustomUser.DoesNotExist:
        #convertesc eroarea in text 
        eroare_text = traceback.format_exc()
        messages.warning(request, 'Utilizatorul nu e logat.')
        mail_admins(
            subject="Eroare majora la profil",
            message=eroare_text,  
            fail_silently=False,
            html_message=f"""
                <div style="background-color:red;">
                    <h2">Eroare</h2>
                    <pre>{eroare_text}</pre>
                </div>
            """
        )
        
        # Daca user-ul nu exista, il deconectam
        logout(request)
        return redirect('login') 
        
    context = {
        'profile_data': profile_data
    }
    return render(request, 'magazin_haine/profil.html', context)

from .forms import PromotieForm
from django.core.mail import send_mass_mail

def promotii_view(request):
    if request.method == 'POST':
        form = PromotieForm(request.POST)

        if form.is_valid():
            
            form.save()
            messages.info(request, 'Formular de promotii creat cu succes')
            subiect = form.cleaned_data['subiect']
            mesaj = form.cleaned_data['mesaj']
            categorii_selectate = form.cleaned_data['categorii_valabile']
            minim_accesari = form.cleaned_data['minim_accesari']

            datatuple = []

            # luam toti utilizatorii
            toti_userii = CustomUser.objects.all()
            logger.info('S-au detectat toti users.')
            mesaj2 = ''
            
            for categorie in categorii_selectate:
                for user in toti_userii:

                    viz_cnt = Vizualizare.objects.filter(
                        produs__categorie=categorie,
                        user=user
                    ).count()

                    if viz_cnt >= minim_accesari:
                        datatuple.append((
                            subiect,
                            mesaj,
                            'ioionutza.03vlad@gmail.com',
                            [user.email]
                        ))

            if datatuple:
                send_mass_mail(datatuple, fail_silently=False)
                logger.info('S-a trimis mail cu promotie')

            return redirect('promotii')

    else:
        form = PromotieForm()

    return render(request, 'magazin_haine/promotii.html', {'form': form})



def interzis(request, titlu = 'Interzis', mesaj_personalizat = 'Nu ai permisiune'):    
    # contorizam accesarile 403 in sesiune
    count = request.session.get("count_403", 0)
    count += 1
    request.session["count_403"] = count
    user = None
    
    if request.user :
        user = request.user
        
    return render(request, 'magazin_haine/403.html', {
        'user' : user,
        'titlu' : titlu, 
        'mesaj_personalizat' : mesaj_personalizat,
        'count' : count,
        'n_max' : settings.N_MAX_403,
        }
    )
from django.contrib.auth.models import  Permission


@login_required
def pagina_oferta(request):
    if request.method == 'POST':
        perm = Permission.objects.get(codename='vizualizeaza_oferta')
        request.user.user_permissions.add(perm)
        return redirect('oferta')
    return HttpResponseForbidden("Acces interzis")

@login_required
def oferta(request):
    if not request.user.has_perm('magazin_haine.vizualizeaza_oferta'):
        return HttpResponseForbidden(render(
            request,
            'magazin_haine/403.html',
            {
                'titlu': 'Eroare afisare oferta',
                'mesaj_personalizat': 'Nu ai voie să vizualizezi oferta'
            }
        ))

    #return render(request, 'magazin_haine/oferta.html')
    return HttpResponse(request, '<h2>Super Oferta</h2>')


