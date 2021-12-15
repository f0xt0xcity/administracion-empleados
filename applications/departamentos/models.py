from django.db import models

# Create your models here.
class Departamentos(models.Model):
    name = models.CharField(max_length=200, verbose_name = "Nombre del departamento")
    shor_name = models.CharField(max_length=20, verbose_name = "Nombre Corto")
    anulate = models.BooleanField(verbose_name="Anulado", default=False)


    class Meta:
        verbose_name = "Mi Departamento"
        verbose_name_plural = "Areas de la empresa"
        ordering = ["-name"]
        unique_together = ('name','shor_name')

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shor_name