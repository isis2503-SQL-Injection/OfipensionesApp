from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings
from random import uniform, choice

class Command(BaseCommand):
    help = 'Crear cuentas asociadas a cada estudiante en MongoDB'

    def handle(self, *args, **kwargs):
        # Conectar a MongoDB
        client = MongoClient(settings.MONGO_CLI)
        db = client['ofipensionesdb']  # Base de datos
        estudiantes_collection = db['estudiantes']  # Colección de estudiantes
        cuentas_collection = db['cuentas']  # Colección de cuentas

        # Obtener todos los estudiantes
        estudiantes = list(estudiantes_collection.find({}))
        if not estudiantes:
            self.stdout.write(self.style.ERROR('No hay estudiantes en la base de datos.'))
            client.close()
            return

        cuentas_creadas = 0
        for estudiante in estudiantes:
            estudiante_id = estudiante['_id']  # ID único del estudiante

            # Crear una cuenta para el estudiante
            cuenta = {
                "estado": choice(['Activa', 'Suspendida', 'Cerrada']),  # Estados posibles
                "saldoPendiente": round(uniform(0, 5000), 2),  # Saldo pendiente aleatorio
                "estudiante": estudiante_id  # Asociación con el estudiante
            }

            # Insertar la cuenta en la colección "cuentas"
            cuentas_collection.insert_one(cuenta)
            cuentas_creadas += 1

        client.close()  # Cerrar conexión
        self.stdout.write(self.style.SUCCESS(f'Se crearon {cuentas_creadas} cuentas correctamente.'))
