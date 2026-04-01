from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from .utils import encriptar_password
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

@login_required
def lista_virtuales(request):

    servidores = ServidorVirtual.objects.all()
    es_admin = ServidorVirtual.objects.all()

    es_admin = request.user.groups.filter(name="Administradores").exists()

    context = {
        "servidores": servidores,
        "es_admin": es_admin
    }


    sede = request.GET.get("sede")
    hipervisor = request.GET.get("hipervisor")
    os = request.GET.get("os")

    if sede:
        servidores = servidores.filter(Sede=sede)

    if hipervisor:
        servidores = servidores.filter(Hipervizor=hipervisor)

    if os:
        servidores = servidores.filter(O_S=os)

    return render(request, "inventario/lista_virtuales.html", {
        "servidores": servidores
    })

@login_required
def agregar_virtual(request):
    if request.method == "POST":
        form = ServidorVirtualForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_virtuales")
    else:
        form = ServidorVirtualForm()
    return render(request, "inventario/form_virtual.html", {"form": form})

@login_required
def editar_virtual(request, id):
    servidor = get_object_or_404(ServidorVirtual, id=id)
    if request.method == "POST":
        form = ServidorVirtualForm(request.POST, instance=servidor)
        if form.is_valid():
            form.save()
            return redirect("lista_virtuales")
    else:
        form = ServidorVirtualForm(instance=servidor)
    return render(request, "inventario/form_virtual.html", {"form": form})

@login_required
def eliminar_virtual(request, id):

    if not request.user.groups.filter(name="Administradores").exists():
        return redirect("lista_virtuales")

    servidor = ServidorVirtual.objects.get(id=id)

    servidor.delete()

    return redirect("lista_virtuales")
    #equipos = Servidores_Virtuales.objects.all()
    #context = {
    #    "Servidores Vituales": Servidores_Virtuales
    #}
    #return render(request, "inventario/lista_equipos.html", context) #por que funciono?