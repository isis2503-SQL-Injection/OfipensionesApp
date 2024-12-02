from django.core.management.base import BaseCommand
from responsableEconomico.models import ResponsableEconomico

class Command(BaseCommand):
    help = 'Popula la tabla ResponsableEconomico con datos secuenciales'

    def handle(self, *args, **kwargs):
        total_registros = 5000  # Ajusta el número total según sea necesario

        for i in range(1, total_registros + 1):  # Documento comienza en 1 y termina en total_registros
            ResponsableEconomico.objects.create(
                documentoIdentidad=str(i),  # Documento secuencial como cadena
                saldoPendiente=round(1000.0 + (i % 100) * 10.5, 2)  # Saldo pendiente ajustado de ejemplo
            )

            # Mostrar progreso cada 100 registros
            if i % 100 == 0:
                self.stdout.write(f'{i}/{total_registros} registros creados.')

        self.stdout.write(self.style.SUCCESS('Población completada con éxito.'))
