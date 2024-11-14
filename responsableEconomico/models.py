# responsableEconomico/models.py
from django.db import models

class ResponsableEconomico(models.Model):
    documentoIdentidad = models.CharField(max_length=100)
    saldoPendiente = models.FloatField(null = False, blank = False)

    objects = models.Manager()
    
 