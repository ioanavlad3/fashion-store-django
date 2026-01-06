import schedule
import time
import django
import os

from datetime import timedelta
import random
from django.core.mail import send_mail

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magazin.settings')
django.setup()


from django.utils import timezone
from .models import CustomUser
import logging

from django.conf import settings
logger = logging.getLogger('django')


def sterge_users():
    users_inactivi = CustomUser.objects.filter(email_confirmat = False)
    
    for user in users_inactivi:
        logger.warning(
                f"Utilizator sters: {user.username}"
            )
        user.delete()
        
        

MESAJ_PROMOTII = [
    "Reduceri exclusive la produsele din magazin!",
    "Descopera cele mai noi articole din colectia noastra!",
    "Promotii limitate disponibile doar astazi!",
    "Nu rata ofertele saptamanii!",
    "Cele mai frumoase haine, doar la Aurore Boutique!"
]

def trimite_mail():
        now = timezone.now()
        limita = now - timedelta(
            minutes=settings.NEWSLETTER_UTILIZATOR_MINUTE
        )
        
        users = CustomUser.objects.filter(
            date_joined__lte=limita,
            is_active=True
        )
        
        for user in users:
            mesaj = random.choice(MESAJ_PROMOTII)

            continut = f"""
            Salut {user.username},

            {mesaj}

            Intra pe site-ul nostru, Aurore Boutique, si vezi cele mai noi produse!
            """

            send_mail(
                subject="Newsletter Aurore Boutique",
                message=continut,
                from_email='ioionutza.03vlad@gmail.com',
                recipient_list=[user.email],
                fail_silently=True,
            )

            logger.info(
                f"Newsletter trimis catre {user.email}"
            )
            
# atentionez utilizatorii care inca nu si-au confirmat adresa de mail ca li se va inchide contul curand
def atentioneaza_users():
    users_inactivi = CustomUser.objects.filter(email_confirmat = False)
    
    for user in users_inactivi:
        send_mail(
            subject="Atentie! Confirma mailul!",
            message='Daca nu confirmi curand adresa de email, atunci contul ti se va inchide.',
            from_email='ioionutza.03vlad@gmail.com',
            recipient_list=[user.email],
            fail_silently=True,
        )
        
# cu cat esti mai ativ pe site, cu atat ai mai multe beneficii

from django.core.mail import send_mass_mail

def oferte_promotii():
    users = CustomUser.objects.all()
    datatuple = []
    subiect = 'Nu uita de Aurore Boutique'
    mesaj = 'Cu cat esti mai activ pe site-ul nostru, cu atat ai mai multe promotii'
    for user in users:
        if user.is_active == True:
            datatuple.append((
                                subiect,
                                mesaj,
                                'ioionutza.03vlad@gmail.com',
                                [user.email]
                            ))

    if datatuple:
        send_mass_mail(datatuple, fail_silently=False)
        logger.info('S-a trimis mail cu atentionare la promotii')
