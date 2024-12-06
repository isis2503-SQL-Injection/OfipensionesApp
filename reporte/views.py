from django.http import JsonResponse
from pymongo import MongoClient
from django.conf import settings
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Cuenta
from estudiante.models import Estudiante
from reporte.models import Reporte
from django.utils.dateparse import parse_date
from django.shortcuts import render
from pymongo import MongoClient
from django.conf import settings
from datetime import datetime
from rest_framework.decorators import api_view

@api_view(["GET"])
def reporteEstadoCuenta(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client['ofipensionesdb']  
    estudiantes_collection = db['estudiantes']
    cuentas_collection = db['cuentas']
    reportes_collection = db['reportes']

    try:
        codigo_estudiante = request.GET.get('codigoEstudiante')
        fecha_param = request.GET.get('fecha')

        if not codigo_estudiante or not fecha_param:
            client.close()
            return render(request, 'reporteEstadoCuenta.html', {'error': 'Faltan parámetros'})

        try:
            fecha_limite = datetime.strptime(fecha_param, '%Y-%m-%d')  
        except ValueError:
            client.close()
            return render(request, 'reporteEstadoCuenta.html', {'error': 'Formato de fecha incorrecto'})

        estudiante = estudiantes_collection.find_one({'codigoEstudiante': codigo_estudiante})
        if not estudiante:
            client.close()
            return render(request, 'reporteEstadoCuenta.html', {'error': 'Estudiante no encontrado'})

        cuenta = cuentas_collection.find_one({'estudiante': estudiante['_id']})
        if not cuenta:
            client.close()
            return render(request, 'reporteEstadoCuenta.html', {'error': 'Cuenta no encontrada'})

        reportes = reportes_collection.find({
            'cuentas': cuenta['_id'],
            'fechaEmision': {'$lte': fecha_limite}
        })

        reportes_data = [
            {
                'fecha_emision': reporte['fechaEmision'],
                'descripcion': reporte['descripcion'],
            }
            for reporte in reportes
        ]

        client.close()

        return render(request, 'reporteEstadoCuenta.html', {
            'codigo_estudiante': estudiante['codigoEstudiante'],
            'saldo_pendiente': cuenta['saldoPendiente'],
            'estado_cuenta': cuenta['estado'],
            'reportes': reportes_data,
        })

    except Exception as e:
        client.close()
        return render(request, 'reporteEstadoCuenta.html', {'error': str(e)})

        
        
@api_view(["GET"])
def prueba(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client['ofipensionesdb']  
    reportes = db['reportes']  

    try:
        result = []
        data = reportes.find({})
        for dto in data:
            jsonData = {
                'id': str(dto['_id']),
                'fechaEmision': dto['fechaEmision'],  
                'descripcion': dto['descripcion'],
                'cuentas': dto.get('cuentas', []),  
            }
            result.append(jsonData)
        
        client.close()

        return render(request, 'prueba.html', {'reportes': result})

    except Exception as e:
        client.close()
        return JsonResponse({"error": str(e)}, status=500)