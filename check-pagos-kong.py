import os
import django
from django.core.mail import send_mail
import requests
import time
from ofipensiones.settings import EMAIL_HOST_USER

# Configura el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ofipensiones.settings")
django.setup()

def check_kong_status():
    try:
        response = requests.get("http://10.128.0.51:8000/pagos/health-check")
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def send_failure_email():
    subject = 'FALLA EN OFIPENSIONES'
    message = 'Warning!!! El sistema de pagos está caído!!!!'
    recepient = "ericsalarcond@gmail.com"
    send_mail(subject, message, EMAIL_HOST_USER, [recepient])
    print("Correo de falla enviado exitosamente.")

if __name__ == "__main__":
    while True:
        if not check_kong_status():
            send_failure_email()
            break
        time.sleep(30)
