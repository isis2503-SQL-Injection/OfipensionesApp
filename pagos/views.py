from django.shortcuts import render
from django.utils.dateparse import parse_date
from .models import Pago, Estudiante
from django.http import HttpResponse
from ofipensiones.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from ofipensiones.auth0backend import getRole
from django.contrib.auth.decorators import login_required



def generarReciboPrematricula(request):
    if request.method == 'GET':
        codigo_estudiante = request.GET.get('codigoEstudiante')
        fecha_param = request.GET.get('fecha')

        fecha_limite = parse_date(fecha_param)

        if not codigo_estudiante or not fecha_limite:
            return render(request, 'pagos/reciboPreMatricula.html', {'error': 'Faltan parámetros o formato incorrecto'})

        try:
            estudiante = Estudiante.objects.get(codigoEstudiante=codigo_estudiante)

            pagos_matricula = Pago.objects.filter(
                estudiante=estudiante,
                tipo='matricula',
                estado='noPago',
                matricula__fechaPrematricula__lte=fecha_limite  
            )

            return render(request, 'reciboPreMatricula.html', {
                'pagos': pagos_matricula,
                'estudiante': estudiante,
                'fecha_limite': fecha_limite
            })

        except Estudiante.objects.get(codigoEstudiante=codigo_estudiante).DoesNotExist:
            return render(request, 'reciboPreMatricula.html', {'error': 'Estudiante no encontrado'})

    return render(request, 'reciboPreMatricula.html', {'error': 'Método no permitido'})

def healtCheck(request):
    return HttpResponse('ok')

def menu(request):
    return render(request, 'pagoMenu.html')

def avisar(request):
    
    subject = 'FALLA EN OFIPENSIONES'
    message = 'Warning!!! El sistema de pagos esta caido!!!!'
    recepient = "ericsalarcond@gmail.com"
    send_mail(subject, message, EMAIL_HOST_USER, [recepient])
    
    return render(request, 'index.html')

#Para autenticar con el codigo
@login_required
def VerReciboPrematricula(request):
    codigo_estudiante = request.GET.get('codigoEstudiante')
    role = getRole(request)
    if role == codigo_estudiante:
        estudiante = Estudiante.objects.get(codigoEstudiante=codigo_estudiante)
        pagos_matricula = Pago.objects.filter(
                estudiante=estudiante,
                tipo='matricula',
                estado='noPago'
            )
        context = {
                'pagos': pagos_matricula,
                'estudiante': estudiante
            }        
        return render(request, 'pagos/reciboPreMatricula.html', context)
    else:
        return HttpResponse("Unauthorized User")