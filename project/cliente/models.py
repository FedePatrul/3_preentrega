from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "país"
        verbose_name_plural = "países"


class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    mail = models.CharField(max_length=150)
    pais_origen_id = models.ForeignKey(
        Pais, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="país de origen"
    )

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"