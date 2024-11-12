from django.db import models
from responsableEconomico.models import ResponsableEconomico

class Estudiante(models.Model):
    codigoEstudiante = models.CharField(max_length=100)  
    fechaNacimiento = models.DateTimeField(null = False, blank = False)  
    grado = models.CharField(max_length=100) 
    objects = models.Manager()
    responsable_economico = models.ForeignKey(ResponsableEconomico,on_delete=models.CASCADE, related_name='estudiantes')
    
    

    