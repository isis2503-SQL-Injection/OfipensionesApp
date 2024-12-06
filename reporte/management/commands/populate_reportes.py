from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings
from datetime import datetime, timedelta
from random import randint

class Command(BaseCommand):
    help = 'Crear reportes asociados a cuentas en MongoDB'

    def handle(self, *args, **kwargs):
        # Conectar a MongoDB
        client = MongoClient(settings.MONGO_CLI)
        db = client['ofipensionesdb']  # Base de datos
        cuentas_collection = db['cuentas']  # Colección de cuentas
        reportes_collection = db['reportes']  # Colección de reportes

        # Obtener todas las cuentas
        cuentas = list(cuentas_collection.find({}))
        if not cuentas:
            self.stdout.write(self.style.ERROR('No hay cuentas en la base de datos.'))
            return

        reportes_creados = 0
        for cuenta in cuentas:
            cuenta_id = cuenta['_id']  # ID único de la cuenta

            # Crear reportes para cada cuenta
            num_reportes = 2  # Número de reportes por cuenta
            for i in range(num_reportes):
                fecha_emision = datetime.now() - timedelta(days=randint(0, 365))  # Fecha aleatoria en el último año
                descripcion = f"Reporte {i+1} para Cuenta {cuenta_id}"

                # Crear reporte en la colección "reportes"
                reporte = {
                    "fechaEmision": fecha_emision.isoformat(),  # Convertir fecha a string ISO
                    "descripcion": descripcion,
                    "cuentas": [cuenta_id]  # Asociar la cuenta al reporte
                }
                reportes_collection.insert_one(reporte)  # Insertar el reporte en MongoDB
                reportes_creados += 1

        client.close()  # Cerrar conexión
        self.stdout.write(self.style.SUCCESS(f'Se crearon {reportes_creados} reportes correctamente.'))
