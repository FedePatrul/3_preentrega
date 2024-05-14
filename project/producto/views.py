from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def index(request):
    return render(request, "producto/index.html")

def producto_list(request):
    busqueda = request.GET.get ("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Producto.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = Producto.objects.all()
    contexto = {"productos": consulta}
    return render(request, "producto/producto_list.html", contexto)

def producto_create(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:list")
    else:
        form = ProductoForm()
    return render(request, "producto/producto_form.html", {"form": form})

def producto_detail(request, pk: int):
    consulta = Producto.objects.get(id=pk)
    contexto = {"producto": consulta}
    return render(request, "producto/producto_detail.html", contexto)

def producto_update(request, pk: int):
    consulta = Producto.objects.get(id=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("producto:list")
    else:
        form = ProductoForm(instance=consulta)
    return render(request, "producto/producto_form.html", {"form": form})

def producto_delete(request, pk: int):
    consulta = Producto.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("producto:list")
    else:
        return render(request, "producto/producto_confirm_delete.html", {"object":consulta})