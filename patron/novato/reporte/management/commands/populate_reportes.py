from django.core.management.base import BaseCommand
from reporte.models import Reporte
from cuenta.models import Cuenta
from datetime import datetime, timedelta
from random import randint

class Command(BaseCommand):
    help = 'Crear reportes asociados a cuentas'

    def handle(self, *args, **kwargs):
        cuentas = Cuenta.objects.all()

        if cuentas.count() == 0:
            self.stdout.write(self.style.ERROR('No hay cuentas en la base de datos.'))
            return

        reportes_creados = 0
        for cuenta in cuentas:
            # Crear reportes para cada cuenta
            num_reportes = 2  # Número de reportes por cuenta
            for i in range(num_reportes):
                fecha_emision = datetime.now() - timedelta(days=randint(0, 365))  # Fecha aleatoria en el último año
                reporte = Reporte.objects.create(
                    fechaEmision=fecha_emision,
                    descripcion=f"Reporte {i+1} para Cuenta {cuenta.id}",
                )
                # Asociar el reporte a la cuenta
                reporte.cuentas.add(cuenta)
                reportes_creados += 1

        self.stdout.write(self.style.SUCCESS(f'Se crearon {reportes_creados} reportes correctamente.'))
