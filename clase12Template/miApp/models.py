from django.db import models

class Book(models.Model):
    nombre=models.CharField(max_length=100, verbose_name ="Juan")

    def __str__(self):
        return self.nombre
    