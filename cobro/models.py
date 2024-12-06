from django.db import models
from cuenta.models import Cuenta

class Cobro(models.Model):
    monto_pago = models.FloatField() 
    fecha_pago = models.DateTimeField() 
    cuenta = models.OneToOneField(Cuenta, on_delete=models.CASCADE, related_name='cobro') 
    objects = models.Manager()

    def __str__(self):
        return f'Cobro de {self.monto_pago} realizado el {self.fecha_pago}'
