from django.db import models
from ckeditor.fields import RichTextField
from applications.departamentos.models import Departamentos
# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField(max_length=20, verbose_name='Habilidad')

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades empleado"
    def __str__(self):
         return self.habilidad


class Empleado(models.Model):
    """
    Modelo para tabla empleado
    """
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('3', 'Economista'),
        ('4', 'Otro'),
    )
    first_name = models.CharField(max_length=60, verbose_name = "Nombres")
    last_name = models.CharField(max_length=60, verbose_name = "Apellidos")
    fullname = models.CharField(
        verbose_name = "Nombre completo",
        max_length= 120,
        blank = True,
    )
    job  = models.CharField(max_length=50, choices=JOB_CHOICES, verbose_name="Trabajo")
    departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE, verbose_name="Departamento")
    avatar = models.ImageField(upload_to="empleado",verbose_name="Imagen del trabajador", null=True, blank=True)
    habilidades = models.ManyToManyField(Habilidades, verbose_name='Habilidades del empleado')
    hoja_vida = RichTextField(blank=True, null = True )

    class Meta:
        verbose_name = "Mi empleado"
        verbose_name_plural = "Empleados de la empresa"
        ordering = ["-first_name"]
        unique_together = ('first_name','last_name')


    def __str__(self):
        return str(self.id) + "-" + self.first_name + "-" + self.last_name