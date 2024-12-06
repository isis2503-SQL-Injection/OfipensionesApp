from django.shortcuts import render
import pika
from estudiante.models import Estudiante
from descuento.models import Descuento
import json
from django.utils.dateparse import parse_date
from django.http import JsonResponse


def nuevo_descuento(request):
    if request.method == "POST":
        try:
     
            data = json.loads(request.body)
            
            estudiante_id = data.get("estudiante_id")
            mes = parse_date(data.get("mes")) 
            porcentaje = data.get("porcentaje")  

            if not estudiante_id or not mes or porcentaje is None:
                return JsonResponse({'error': 'Faltan parametros'}, status=400)
            estudiante = Estudiante.objects.get(id=estudiante_id)

            descuento = Descuento.objects.create(
                estudiante=estudiante,
                mes=mes,
                porcentaje=porcentaje
            )

            return JsonResponse({
                "message": "Descuento added successfully",
                "descuento": {
                    "id": descuento.id,
                    "estudiante_id": descuento.estudiante.id,
                    "mes": descuento.mes.strftime("%Y-%m-%d"),
                    "porcentaje": float(descuento.porcentaje)
                }
            }, status=201)

        except Estudiante.DoesNotExist:
            return JsonResponse({"error": "Estudiante not found"}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)