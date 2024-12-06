from django.db import models
from cuenta.models import Cuenta

class Reporte(models.Model):
    fechaEmision = models.DateTimeField()
    descripcion = models.CharField(max_length=50)   
    cuentas = models.ManyToManyField(Cuenta, related_name='reportes')
    objects = models.Manager()
    
