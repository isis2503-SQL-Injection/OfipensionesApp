from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from estudiante.models import Estudiante
from dj_cqrs.mixins import MasterMixin

class Descuento(MasterMixin, models.Model):
    CQRS_ID = 'descuento-model'
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='descuentos')
    mes = models.DateField()
    porcentaje = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
def save(self, *args, **kwargs):
        
        self.date = self.date.replace(day=1)
        super().save(*args, **kwargs)

def __str__(self):
    return f"ID: {self.id}, Date: {self.date.strftime('%Y-%m')}, Porcentaje: {self.porcentaje}%"