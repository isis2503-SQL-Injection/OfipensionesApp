from django.db import models
from pagos.models import Pago

class ReciboPago(models.Model):
    pagos = models.ManyToManyField(Pago, related_name='recibos')
    fechaEmision = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
