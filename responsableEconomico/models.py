# responsableEconomico/models.py
from django.db import models

class ResponsableEconomico(models.Model):
    documento_identidad = models.CharField(max_length=100)  
    relacionConEstudiante = models.CharField(max_length=100) 
    saldoPendiente = models.FloatField(null = False, blank = False)
