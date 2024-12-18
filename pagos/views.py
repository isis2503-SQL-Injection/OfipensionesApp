from django.shortcuts import render
from django.utils.dateparse import parse_date
from .models import Pago, Estudiante
from django.http import HttpResponse
from ofipensiones.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from ofipensiones.auth0backend import getRole
from django.contrib.auth.decorators import login_required
from estudiante.models import Estudiante
from responsableEconomico.models import ResponsableEconomico

@login_required
def generarReciboPrematricula(request):
    if request.method == 'GET':
        cedulaResponsable = getRole(request)        
        codigo_estudiante = request.GET.get('codigoEstudiante')
        
        if verificar_responsable(cedulaResponsable, codigo_estudiante) == False:
            return render(request, 'accesoDenegado.html', {'error': 'No tiene permisos para ver este contenido'})
        
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

@login_required
def menu(request):
    return render(request, 'pagoMenu.html')

def avisar(request):
    
    subject = 'FALLA EN OFIPENSIONES'
    message = 'Warning!!! El sistema de pagos esta caido!!!!'
    recepient = "ericsalarcond@gmail.com"
    send_mail(subject, message, EMAIL_HOST_USER, [recepient])
    
    return render(request, 'index.html')

def verificar_responsable(documento_identidad, codigo_estudiante):
   
    responsable = ResponsableEconomico.objects.get(documentoIdentidad=documento_identidad)
        
    estudiante = Estudiante.objects.get(codigoEstudiante=codigo_estudiante)
        
    if estudiante.responsable_economico == responsable:
        return True 
    else:
        return False  
   
