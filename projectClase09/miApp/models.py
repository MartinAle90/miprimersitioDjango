from django.db import models

class Book(models.Model):
    nombre=models.CharField(max_length=500)
    autor=models.CharField(max_length=200)
    disponible=models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre