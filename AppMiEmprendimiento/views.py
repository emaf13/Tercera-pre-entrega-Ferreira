from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "AppMiEmprendimiento/index.html")

def proveedores(request):
    return render(request, "AppMiEmprendimiento/proveedores.html")

def pedidos(request):
    return render(request, "AppMiEmprendimiento/pedidos.html")

def clientes(request):
    return render(request, "AppMiEmprendimiento/clientes.html")

def ventas(request):
    return render(request, "AppMiEmprendimiento/ventas.html")
