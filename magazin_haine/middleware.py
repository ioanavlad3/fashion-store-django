from datetime import datetime
from collections import deque

REQUEST_LOG = deque(maxlen=100)  
COUNT = 0           


days = ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica"]
months = ["Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie",
        "Iulie", "August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie"]

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        global COUNT
        COUNT += 1

        REQUEST_LOG.append({
            "id": COUNT,
            "path": request.path,
            "data": months[datetime.now().month - 1],
            "day": days[datetime.now().weekday()] ,
            'hour' : datetime.now().time
        })
        return self.get_response(request)


class Procesare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        # cod de procesare a cererii ....      
        #putem trimite date către funcția de vizualizare; le setăm ca proprietăți în request     
        request.proprietate_noua=17       
        # se apelează (indirect) funcția de vizualizare (din views.py)
        response = self.get_response(request)      

        # putem adauga un header HTTP pentru toate răspunsurile
        response['header_nou'] = 'valoare'

        # aici putem modifica chiar conținutul răspunsului
        # verificăm tipul de conținut folosind headerul HTTP Content-Type
        # motivul fiind că putem transmite și alte resurse (imagini, css etc.), nu doar fișiere html
        if response.has_header('Content-Type') and 'text/html' in response['Content-Type']:

            # obținem conținutul
            # (response.content este memorat ca bytes, deci îl transformăm în string)
            content = response.content.decode('utf-8')

            # Modificăm conținutul
            # new_content = content.replace(
            #     '</body>',
            #     '<div>Continut suplimentar</div></body>'
            # )

            # Suprascriem conținutul răspunsului
            # response.content = new_content.encode('utf-8')

            # Actualizăm lungimea conținutului (obligatoriu, fiind header HTTP)
            #response['Content-Length'] = len(response.content)

        return response
    
class IPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # preluăm IP-ul utilizatorului
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR', '')

        # salvăm IP-ul ca proprietate pe request
        request.client_ip = ip

        # apelăm view-ul
        response = self.get_response(request)

        return response
