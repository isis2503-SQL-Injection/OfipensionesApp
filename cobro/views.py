from django.shortcuts import render
from pymongo import MongoClient
from django.conf import settings
from rest_framework.decorators import api_view

def index(request):
    return render(request, 'cobroMenu.html')

@api_view(["GET"])
def cobros(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client['ofipensionesdb']  
    cobros_collection = db['cobros']

    try:
        result = []
        cobros = cobros_collection.find({})
        for cobro in cobros:
            jsonData = {
                'id': str(cobro['_id']),
                'monto_pago': cobro['monto_pago'],
                'fecha_pago': cobro['fecha_pago'],
                'cuenta_id': str(cobro['cuenta']), 
            }
            result.append(jsonData)

        client.close()

        return render(request, 'cobros.html', {'cobros': result})

    except Exception as e:
        client.close()
        return render(request, 'cobros.html', {'error': str(e)})
