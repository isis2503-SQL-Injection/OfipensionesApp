from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from estudiante.models import Estudiante
from dj_cqrs.mixins import MasterMixin

class Descuento(MasterMixin, models.Model):
    CQRS_ID = 'descuento-model'
    CQRS_CUSTOM_SERIALIZATION = True

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
    def __str__(self):
        return '%s %s' % (self.value, self.unit)
    
    @staticmethod
    def _handle_variable(mapped_data):
        des = Descuento.objects.get(pk=mapped_data)
        return des
    
    @classmethod
    def cqrs_create(cls, sync, mapped_data, previous_data=None, meta=None):
        print(mapped_data['descuento'])
        descuento = cls._handle_variable(mapped_data['descuento'])
        return Descuento.objects.create(
            id=mapped_data['id'],
            descuento=descuento,
            estudiante_id=mapped_data['estudiante_id'],
            mes=mapped_data['mes'],
            porcentaje=mapped_data['porcentaje'],
            cqrs_revision=mapped_data['cqrs_revision'],
            cqrs_updated=mapped_data['cqrs_updated'],
        )
    
    def cqrs_update(self, sync, mapped_data, previous_data=None, meta=None):
        descuento = self._handle_variable(mapped_data['descuento'])
        self.estudiante_id = mapped_data['estudiante_id']
        self.variabldescuentoe = descuento
        self.mes = mapped_data['mes']
        self.porcentaje = mapped_data['porcentaje']
        self.cqrs_revision = mapped_data['cqrs_revision']
        self.cqrs_updated = mapped_data['cqrs_updated']
        self.save()
        return self