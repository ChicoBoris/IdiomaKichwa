# Aplicaciones/Actividades/models.py
from django.db import models

class Palabra(models.Model):
    id=models.AutoField(primary_key=True)
    quechua = models.CharField(max_length=50)
    espanol = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150,default='') 

    def __str__(self):
        return f"{self.quechua} - {self.espanol}"