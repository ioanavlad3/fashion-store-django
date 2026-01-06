import schedule
import time
import django
import os
import sys
from magazin_haine import tasks
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magazin.settings')
django.setup()

from django.conf import settings
K_MIN_STERGERE = settings.K_MIN_STERGERE
ZI = settings.ZI
ORA = settings.ORA
M = settings.M
ORA2 = settings.ORA2
ZI2 = settings.ZI2

def run_scheduler():
    schedule.every(K_MIN_STERGERE).minutes.do(tasks.sterge_users)
    if ZI.lower() == 'luni':
        schedule.every().monday.at(ORA).do(tasks.trimite_mail) 
    if ZI.lower() == 'marti':
        schedule.every().tuesday.at(ORA).do(tasks.trimite_mail)  
    if ZI.lower() == 'miercuri':
        schedule.every().wednesday.at(ORA).do(tasks.trimite_mail)  
    if ZI.lower() == 'joi':
        schedule.every().thursday.at(ORA).do(tasks.trimite_mail)
    if ZI.lower() == 'vineri':
        schedule.every().friday.at(ORA).do(tasks.trimite_mail)  
    if ZI.lower() == 'sambata':
        schedule.every().saturday.at(ORA).do(tasks.trimite_mail)  
    if ZI.lower() == 'duminica':
        schedule.every().sunday.at(ORA).do(tasks.trimite_mail)  
        
        
    if ZI2.lower() == 'luni':
        schedule.every().monday.at(ORA2).do(tasks.oferte_promotii) 
    if ZI2.lower() == 'marti':
        schedule.every().tuesday.at(ORA2).do(tasks.oferte_promotii)  
    if ZI2.lower() == 'miercuri':
        schedule.every().wednesday.at(ORA2).do(tasks.oferte_promotii)  
    if ZI2.lower() == 'joi':
        schedule.every().thursday.at(ORA2).do(tasks.oferte_promotii)
    if ZI2.lower() == 'vineri':
        schedule.every().friday.at(ORA2).do(tasks.oferte_promotii)  
    if ZI2.lower() == 'sambata':
        schedule.every().saturday.at(ORA2).do(tasks.oferte_promotii)  
    if ZI2.lower() == 'duminica':
        schedule.every().sunday.at(ORA2).do(tasks.oferte_promotii)  
        
        
    schedule.every(M).minute.do(tasks.atentioneaza_users)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    try:
        run_scheduler()
    except KeyboardInterrupt:
        print("Scheduler oprit manual.")
        sys.exit()
