from django.db import models

class Book(models.Model):
    nombre=models.CharField(max_length=100, verbose_name ="Titulo")
    autor=models.CharField(max_length=100, blank=True)
    disponible=models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre