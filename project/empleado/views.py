from django.shortcuts import render, redirect
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.
def index(request):
    return render(request, "empleado/index.html")

def empleado_list(request):
    consulta = Empleado.objects.all()
    contexto = {"empleados": consulta}
    return render(request, "empleado/empleado_list.html", contexto)

def empleado_create(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("empleado:list")
    else:
        form = EmpleadoForm()
    return render(request, "empleado/empleado_form.html", {"form": form})

def empleado_detail(request, pk: int):
    consulta = Empleado.objects.get(id=pk)
    contexto = {"empleado": consulta}
    return render(request, "empleado/empleado_detail.html", contexto)

def empleado_update(request, pk: int):
    consulta = Empleado.objects.get(id=pk)
    if request.method == "POST":
        form = EmpleadoForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("empleado:list")
    else:
        form = EmpleadoForm(instance=consulta)
    return render(request, "empleado/empleado_form.html", {"form": form})

def empleado_delete(request, pk: int):
    consulta = Empleado.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("empleado:list")
    else:
        return render(request, "empleado/empleado_confirm_delete.html", {"object":consulta})