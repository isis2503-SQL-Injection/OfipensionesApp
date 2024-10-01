from django.db import models

class Estudiante(models.Model):
    codigoEstudiante = models.CharField(max_length=100)  
    fechaNacimiento = models.DateTimeField(null = False, blank = False)  
    grado = models.CharField(max_length=100) 
    objects = models.Manager()

    
    

    