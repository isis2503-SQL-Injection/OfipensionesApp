from django.shortcuts import render

from django.shortcuts import render
from django.utils.dateparse import parse_date
from .models import Cuenta
from pagos.models import Pago
from matricula.models import Matricula
from estudiante.models import Estudiante

def reporteSaldoPendienteCuenta(request):
    if request.method == 'GET':
        codigo_estudiante = request.GET.get('codigoEstudiante')
        fecha_param = request.GET.get('fecha')

        fecha_limite = parse_date(fecha_param)

        if not codigo_estudiante or not fecha_limite:
            return render(request, 'reporteSaldoPendienteCuenta.html', {'error': 'Faltan parámetros o formato incorrecto'})

        try:
            estudiante = Estudiante.objects.get(codigoEstudiante=codigo_estudiante)

            cuenta = Cuenta.objects.get(estudiante=estudiante)

            pagos_no_pagados = Pago.objects.filter(
                cuenta=cuenta,
                estado='noPago',
                matricula__fechaLimite__lte=fecha_limite  
            )

            return render(request, 'reporteSaldoPendienteCuenta.html', {
                'codigo_estudiante': estudiante.codigoEstudiante,
                'saldo_pendiente': cuenta.saldoPendiente,
                'pagos': pagos_no_pagados
            })

        except Estudiante.objects.get(codigoEstudiante=codigo_estudiante).DoesNotExist:
            return render(request, 'reporteSaldoPendienteCuenta.html', {'error': 'Estudiante no encontrado'})

        except Cuenta.objects.get(estudiante=estudiante).DoesNotExist:
            return render(request, 'reporteSaldoPendienteCuenta.html', {'error': 'Cuenta no encontrada'})

    return render(request, 'reporteSaldoPendienteCuenta.html', {'error': 'Método no permitido'})

