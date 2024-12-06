from django.shortcuts import render
import pika
from estudiante.models import Estudiante
from descuento.models import Descuento
import json
from django.utils.dateparse import parse_date
from django.http import JsonResponse


def revisarDescuentos(request):
    if request.method == 'GET':
        codigo_estudiante = request.GET.get('codigoEstudiante')

        if not codigo_estudiante:
            return render(request, 'reporteDescuento.html', {'error': 'Falta el estudiante'})
        try:

            estudiante = Estudiante.objects.get(codigoEstudiante=codigo_estudiante)
            descuentos = Descuento.objects.filter(codigo_estudiante=codigo_estudiante)
            
        
            Informacion_descuento = [
                    {
                        'fecha_emision': desc.mes,
                        'Porcentaje de descuento': desc.porcentage
                    }
                    for desc in descuentos
                ]
            return render(request, 'reporteEstadoCuenta.html', {
                'codigo_estudiante': estudiante.codigoEstudiante,
                'reportes': Informacion_descuento,

            })

        except Estudiante.objects.get(codigoEstudiante=codigo_estudiante).DoesNotExist:
            return render(request, 'reporteEstadoCuenta.html', {'error': 'Estudiante no encontrado'})

    return render(request, 'reporteEstadoCuenta.html', {'error': 'Método no permitido'})
