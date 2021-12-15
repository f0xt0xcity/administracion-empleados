from django.db import models

# Create your models here.
class Prueba(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    subtitulo = models.CharField(max_length=50, verbose_name="Subitulo")
    cnatidad = models.IntegerField(verbose_name="Cantidad")

    def __str__(self):
        return self.titulo