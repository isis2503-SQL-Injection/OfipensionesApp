from django.db import models
from pagos.models import Pago

class Matricula(models.Model):
    fechaPrematricula = models.DateTimeField(null = False, blank = False)
    fechaLimite = models.DateTimeField(null = False, blank = False)
    periodoAcademico = models.CharField(max_length = 50, null = False, blank = False)
    pago = models.OneToOneField(Pago, on_delete=models.CASCADE, primary_key=True)
    objects = models.Manager()

    