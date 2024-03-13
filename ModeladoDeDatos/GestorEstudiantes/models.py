from django.db import models

class Estudiante(models.Model):
    nombreEst=models.CharField(max_length=200)
    apellidoEst=models.CharField(max_length=200)
    edadEst=models.IntegerField()
    notaEst=models.IntegerField()

    def __str__(self):
        return self.nombreEst