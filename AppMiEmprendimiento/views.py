from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("INICIO")

def proveedores(request):
    return HttpResponse("Vista proveedores")

def pedidos(request):
    return HttpResponse("Vista pedidos")

def clientes(request):
    return HttpResponse("Vista clientes")

def ventas(request):
    return HttpResponse("Vista ventas")
