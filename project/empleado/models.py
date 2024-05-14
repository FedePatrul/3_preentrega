from django.db import models

# Create your models here.
class Puesto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "puesto"
        verbose_name_plural = "puestos"


class Empleado(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    mail = models.CharField(max_length=150)
    puesto_id = models.ForeignKey(
        Puesto, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Puesto de trabajo"
    )

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "empleado"
        verbose_name_plural = "empleados"