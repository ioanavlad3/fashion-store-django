from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap

from django.contrib.sitemaps import GenericSitemap
from .sitemaps import StaticViewSitemap

from .models import Categorie, Produs

categorie_info = {
    'queryset': Categorie.objects.all(),
}

produs_info = {
    'queryset': Produs.objects.all(),
}

sitemaps = {
    'categorii': GenericSitemap(categorie_info),
    'produse': GenericSitemap(produs_info),
    'static': StaticViewSitemap(),
}


urlpatterns = [
	path("", views.index, name="index"),
    path("info/", views.info, name = "info"),
    path("afisare/", views.afisare, name = "afisare"),
    path("exemplu/", views.afis_template, name = "exemplu"),
    path("simplu/", views.afis_template2, name = "simplu"),
    path("log/", views.log, name = "log"),
    path("locatie/", views.afis_loc, name = "locatie"),
    path("principala/", views.principala, name = "principala"),
    path("despre/", views.despre, name = "despre"),
    path("in_lucru/", views.in_lucru, name = "in_lucru"),
    path('colectii/', views.colectii, name = 'colectii'),
    path('brands/', views.brands, name = 'brands'),
    # path("/lista_produse", views.lista_produse, name = "lista_produse"),
    # path("produs/<uuid:id_produs>/", views.detalii_produs, name = "detalii"),
    path("produs/<uuid:id_varianta>/", views.detalii_produs, name = "detalii"),
    path("categorii/", views.lista_categorii, name = "categorii"),
    path("categorii/<str:nume_categorie>/", views.detalii_categorie, name = "detalii_categorie"),
    path("lista_produse/", views.produs_view, name = "lista_produse"),
    path('contact/', views.contact_view, name = 'contact'),
    path('adauga_produse/', views.adauga_produse, name = 'adauga_produse'),
    path('inregistrare/', views.inregistrare_view, name = 'inregistrare'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name='logout'),
    path('profil/', views.profil_view, name = 'profil'),
    path("confirma_mail/<str:cod_user>/", views.confirma_mail, name = 'confirma_mail'),
    path("cont/", views.cont, name = "cont"),
    path('promotii/', views.promotii_view, name = 'promotii'),
    path('interzis/', views.interzis, name = 'interzis'),
    path('pagina_oferta/', views.pagina_oferta, name = 'pagina_oferta'),
    path('sitemap.xml',
        sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    
    path('cos/', views.cos_virtual, name = 'cos'),
    path('comanda/', views.comanda, name = 'comanda'),
]

handler404 = 'magazin_haine.views.error_404_view'
