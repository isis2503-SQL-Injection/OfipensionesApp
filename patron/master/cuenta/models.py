from django.db import models
from estudiante.models import Estudiante

class Cuenta(models.Model):
    estado = models.CharField(max_length=50)
    saldoPendiente = models.FloatField()
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE, related_name='cuenta')
    objects = models.Manager()

