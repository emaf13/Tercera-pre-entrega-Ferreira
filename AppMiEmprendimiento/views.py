from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "AppMiEmprendimiento/index.html")

def proveedores(request):
    return render(request, "AppMiEmprendimiento/proveedor_test.html")

def pedidos(request):
    return HttpResponse("Vista pedidos")

def clientes(request):
    return render(request, "AppMiEmprendimiento/cliente_test.html")

def ventas(request):
    return HttpResponse("Vista ventas")
