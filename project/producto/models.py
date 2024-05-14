from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    origen = models.CharField(max_length=150)
    precio = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.nombre}"

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"