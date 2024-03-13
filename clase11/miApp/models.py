from django.db import models

# Create your models here.
class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, default="default", verbose_name ="CAT")
    precio = models.IntegerField(max_length=7)
    color = models.CharField(max_length=100)


    def __str__(self):
        return self.titulo