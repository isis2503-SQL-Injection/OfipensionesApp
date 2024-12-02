from django.core.management.base import BaseCommand
from cuenta.models import Cuenta
from estudiante.models import Estudiante
from random import uniform, choice

class Command(BaseCommand):
    help = 'Crear cuentas asociadas a cada estudiante'

    def handle(self, *args, **kwargs):
        estudiantes = Estudiante.objects.all()

        if estudiantes.count() == 0:
            self.stdout.write(self.style.ERROR('No hay estudiantes en la base de datos.'))
            return

        cuentas_creadas = 0
        for estudiante in estudiantes:
            # Crear cuenta para cada estudiante
            cuenta = Cuenta.objects.create(
                estado=choice(['Activa', 'Suspendida', 'Cerrada']),  # Estados posibles
                saldoPendiente=round(uniform(0, 5000), 2),  # Saldo pendiente aleatorio
                estudiante=estudiante
            )
            cuentas_creadas += 1

        self.stdout.write(self.style.SUCCESS(f'Se crearon {cuentas_creadas} cuentas correctamente.'))
