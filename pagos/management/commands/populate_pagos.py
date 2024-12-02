from django.core.management.base import BaseCommand
from pago.models import Pago
from estudiante.models import Estudiante
from cuenta.models import Cuenta
from random import uniform, choice

class Command(BaseCommand):
    help = 'Crear pagos asociados a estudiantes y cuentas'

    def handle(self, *args, **kwargs):
        estudiantes = Estudiante.objects.all()
        cuentas = Cuenta.objects.all()

        if estudiantes.count() == 0 or cuentas.count() == 0:
            self.stdout.write(self.style.ERROR('No hay estudiantes o cuentas en la base de datos.'))
            return

        pagos_creados = 0
        for estudiante, cuenta in zip(estudiantes, cuentas):
            # Crear pagos para cada estudiante y cuenta
            num_pagos = 3  # Número de pagos por estudiante/cuenta
            for _ in range(num_pagos):
                pago = Pago.objects.create(
                    monto=round(uniform(100, 1000), 2),  # Monto aleatorio entre 100 y 1000
                    estado=choice(['Pendiente', 'Pagado', 'Fallido']),  # Estados posibles
                    tipo=choice(['Efectivo', 'Tarjeta', 'Transferencia']),  # Tipos posibles
                    estudiante=estudiante,
                    cuenta=cuenta
                )
                pagos_creados += 1

        self.stdout.write(self.style.SUCCESS(f'Se crearon {pagos_creados} pagos correctamente.'))
