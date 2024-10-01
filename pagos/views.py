from django.shortcuts import render
from django.utils.dateparse import parse_date
from .models import Pago, Estudiante

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
