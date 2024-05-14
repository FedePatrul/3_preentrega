from django import forms

from . import models

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = models.Empleado
        fields = ["nombre", "apellido", "mail", "puesto_id"]