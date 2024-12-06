from django.shortcuts import render
from .models import Cuenta
from estudiante.models import Estudiante
from reporte.models import Reporte
from django.utils.dateparse import parse_date

def reporteEstadoCuenta(request):
    if request.method == 'GET':
        codigo_estudiante = request.GET.get('codigoEstudiante')
        fecha_param = request.GET.get('fecha')
        fecha_limite = parse_date(fecha_param)

        if not codigo_estudiante or not fecha_limite:
            return render(request, 'reporteEstadoCuenta.html', {'error': 'Faltan parámetros o formato incorrecto'})
        try:

            estudiante = Estudiante.objects.get(codigoEstudiante=codigo_estudiante)
            cuenta = Cuenta.objects.get(estudiante=estudiante)
            reportes = Reporte.objects.filter(cuentas=cuenta, fechaEmision__lte=fecha_limite)
        
            reportes_data = [
                    {
                        'fecha_emision': reporte.fechaEmision,
                        'descripcion': reporte.descripcion,
                    }
                    for reporte in reportes
                ]
            return render(request, 'reporteEstadoCuenta.html', {
                'codigo_estudiante': estudiante.codigoEstudiante,
                'saldo_pendiente': cuenta.saldoPendiente,
                'estado_cuenta': cuenta.estado,
                'reportes': reportes_data,

            })

        except Estudiante.objects.get(codigoEstudiante=codigo_estudiante).DoesNotExist:
            return render(request, 'reporteEstadoCuenta.html', {'error': 'Estudiante no encontrado'})

        except Cuenta.objects.get(estudiante=estudiante).DoesNotExist:
            return render(request, 'reporteEstadoCuenta.html', {'error': 'Cuenta no encontrada'})

    return render(request, 'reporteEstadoCuenta.html', {'error': 'Método no permitido'})
        