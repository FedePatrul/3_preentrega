from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

# Create your views here.
def index(request):
    return render(request, "cliente/index.html")

def cliente_list(request):
    consulta = Cliente.objects.all()
    contexto = {"clientes": consulta}
    return render(request, "cliente/cliente_list.html", contexto)

def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:list")
    else:
        form = ClienteForm()
    return render(request, "cliente/cliente_form.html", {"form": form})

def cliente_detail(request, pk: int):
    consulta = Cliente.objects.get(id=pk)
    contexto = {"cliente": consulta}
    return render(request, "cliente/cliente_detail.html", contexto)

def cliente_update(request, pk: int):
    consulta = Cliente.objects.get(id=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("cliente:list")
    else:
        form = ClienteForm(instance=consulta)
    return render(request, "cliente/cliente_form.html", {"form": form})

def cliente_delete(request, pk: int):
    consulta = Cliente.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("cliente:list")
    else:
        return render(request, "cliente/cliente_confirm_delete.html", {"object":consulta})