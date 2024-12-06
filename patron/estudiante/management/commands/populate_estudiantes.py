from django.core.management.base import BaseCommand
from estudiante.models import Estudiante
from responsableEconomico.models import ResponsableEconomico
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Crear 5000 estudiantes asociados a responsables económicos'

    def handle(self, *args, **kwargs):
        responsables = ResponsableEconomico.objects.all()
        total_responsables = responsables.count()
        
        if total_responsables == 0:
            self.stdout.write(self.style.ERROR('No hay responsables económicos en la base de datos.'))
            return

        estudiantes_creados = 0
        for i in range(1, 5001):
            # Asignar un responsable económico en orden
            responsable = responsables[(i - 1) % total_responsables]
            
            # Crear estudiante
            estudiante = Estudiante.objects.create(
                codigoEstudiante=str(i),
                fechaNacimiento=datetime.now() - timedelta(days=(365 * 18 + i % 365)),  # Fecha simulada
                grado=f'Grado {i % 11 + 1}',  # Grados del 1 al 11
                responsable_economico=responsable
            )
            estudiantes_creados += 1

        self.stdout.write(self.style.SUCCESS(f'Se crearon {estudiantes_creados} estudiantes correctamente.'))
