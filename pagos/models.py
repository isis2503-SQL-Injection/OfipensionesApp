from django.db import models
from estudiante.models import Estudiante
from cuenta.models import Cuenta

class Pago(models.Model):
    monto = models.FloatField(null = False, blank = False)
    estado = models.CharField(max_length = 50, null = False, blank = False)
    tipo = models.CharField(max_length = 50, null = False, blank = False)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='pagos')
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='pagos')
    objects = models.Manager()
