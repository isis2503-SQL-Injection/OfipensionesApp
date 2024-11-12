from django.shortcuts import render
from django.utils.dateparse import parse_date
from .models import Pago, Estudiante
from django.http import HttpResponse
from ofipensiones.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from ofipensiones.auth0backend import getRole
from django.contrib.auth.decorators import login_required
from responsableEconomico.models import ResponsableEconomico


@login_required
def generarReciboPrematricula(request):
    if request.method == 'GET':
        codigo_estudiante = request.GET.get('codigoEstudiante')
        fecha_param = request.GET.get('fecha')

        fecha_limite = parse_date(fecha_param)

        if not codigo_estudiante or not fecha_limite:
            return render(request, 'pagos/reciboPreMatricula.html', {'error': 'Faltan parámetros o formato incorrecto'})

        try:
            
            documento_identidad_responsable = getRole(request)
            responsable = ResponsableEconomico.objects.get(documento_identidad=documento_identidad_responsable)
            estudiantes_asociados = responsable.estudiantes.all()
            estudiante = estudiantes_asociados.filter(codigoEstudiante=codigo_estudiante).first()

            if not estudiante:
                return HttpResponse("Unauthorized User - Estudiante no asociado al responsable económico")

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

        except ResponsableEconomico.DoesNotExist:
            return render(request, 'pagos/reciboPreMatricula.html', {'error': 'Responsable económico no encontrado'})
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
