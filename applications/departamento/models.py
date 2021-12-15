from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField(max_length=200, verbose_name = "Nombre del departamento")
    shor_name = models.CharField(max_length=20, verbose_name = "Nombre Corto")
    anulate = models.BooleanField(verbose_name="Anulado", default=False)

    def __str__(self):
        return self.id + '-' + self.name + '-' + self.shor_name