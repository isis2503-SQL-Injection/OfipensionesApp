from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Crear 5000 estudiantes asociados a responsables económicos en MongoDB'

    def handle(self, *args, **kwargs):
        # Conectar a MongoDB
        client = MongoClient(settings.MONGO_CLI)
        db = client['ofipensionesdb']  # Base de datos
        responsables_collection = db['responsables_economicos']  # Colección de responsables económicos
        estudiantes_collection = db['estudiantes']  # Colección de estudiantes

        # Obtener todos los responsables económicos
        responsables = list(responsables_collection.find({}))
        total_responsables = len(responsables)

        if total_responsables == 0:
            self.stdout.write(self.style.ERROR('No hay responsables económicos en la base de datos.'))
            client.close()
            return

        estudiantes_creados = 0
        batch = []  # Inserción en lotes
        for i in range(1, 5001):
            # Asignar un responsable económico en orden
            responsable = responsables[(i - 1) % total_responsables]

            # Crear estudiante
            estudiante = {
                "codigoEstudiante": str(i),
                "fechaNacimiento": (datetime.now() - timedelta(days=(365 * 18 + i % 365))).isoformat(),
                "grado": f'Grado {i % 11 + 1}',  # Grados del 1 al 11
                "responsable_economico": responsable["_id"],  # ID del responsable económico asociado
            }
            batch.append(estudiante)

            # Insertar en lotes de 100 para mejorar rendimiento
            if len(batch) == 100:
                estudiantes_collection.insert_many(batch)
                batch = []
                estudiantes_creados += 100

        # Insertar los documentos restantes
        if batch:
            estudiantes_collection.insert_many(batch)
            estudiantes_creados += len(batch)

        client.close()  # Cerrar conexión
        self.stdout.write(self.style.SUCCESS(f'Se crearon {estudiantes_creados} estudiantes correctamente.'))
