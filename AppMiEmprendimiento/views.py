from django.shortcuts import render
from AppMiEmprendimiento.models import Proveedor, Cliente, Pedido, Venta
#from AppMiEmprendimiento.forms import ProveedorFormulario, BuscarProveedorFormulario, 
from AppMiEmprendimiento.forms import *

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

# def formulario_proveedores(request):
#     return render(request, "AppMiEmprendimiento/proveedores_formulario.html")

 
def alta_proveedores(request):
    if request.method == "POST":
        miFormulario = ProveedorFormulario(request.POST) # Creo una instancia de ProveedorFormulario con la informacion que llega del html 
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            prov = Proveedor(nombre=info["nombre"], telefono=info["telefono"], correo=info["correo"], hacen_envios=info["hacen_envios"])
            prov.save()
            return render(request, "AppMiEmprendimiento/index.html")
    else:
        miFormulario = ProveedorFormulario()
 
    return render(request, "AppMiEmprendimiento/proveedores_alta.html", {"miFormulario": miFormulario})

def buscar_proveedores(request):
    if request.method == "POST":
        miFormulario = BuscarProveedorFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            provs = Proveedor.objects.filter(nombre__icontains=info["nombre"])
            return render(request, "AppMiEmprendimiento/proveedores_resultados.html", {"proveedores": provs})
    else:
        miFormulario = BuscarProveedorFormulario()
 
    return render(request, "AppMiEmprendimiento/proveedores_buscar.html", {"miFormulario": miFormulario})

def alta_clientes(request):
    if request.method == "POST":
        miFormulario = ClienteFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            cliente = Cliente(nombre=info["nombre"], telefono=info["telefono"], correo=info["correo"], apellido=info["apellido"])
            cliente.save()
            return render(request, "AppMiEmprendimiento/index.html")
    else:
        miFormulario = ClienteFormulario()
 
    return render(request, "AppMiEmprendimiento/clientes_alta.html", {"miFormulario": miFormulario})

def buscar_clientes(request):
    if request.method == "POST":
        miFormulario = BuscarClienteFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            cliente = Cliente.objects.filter(nombre__icontains=info["nombre"])
            return render(request, "AppMiEmprendimiento/clientes_resultados.html", {"clientes": cliente})
    else:
        miFormulario = BuscarClienteFormulario()
 
    return render(request, "AppMiEmprendimiento/clientes_buscar.html", {"miFormulario": miFormulario})

def alta_pedidos(request):
    if request.method == "POST":
        miFormulario = PedidoFormulario(request.POST) 
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            ped = Pedido(numero=info["numero"], valor=info["valor"], fecha=info["fecha"])
            ped.save()
            return render(request, "AppMiEmprendimiento/index.html")
    else:
        miFormulario = PedidoFormulario()
 
    return render(request, "AppMiEmprendimiento/pedidos_alta.html", {"miFormulario": miFormulario})

def buscar_pedidos(request):
    if request.method == "POST":
        miFormulario = BuscarPedidoFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            pedidos = Pedido.objects.filter(fecha__icontains=info["fecha"])
            return render(request, "AppMiEmprendimiento/pedidos_resultados.html", {"pedidos": pedidos})
    else:
        miFormulario = BuscarPedidoFormulario()
 
    return render(request, "AppMiEmprendimiento/pedidos_buscar.html", {"miFormulario": miFormulario})

def alta_ventas(request):
    if request.method == "POST":
        miFormulario = VentaFormulario(request.POST) 
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            ven = Venta(numero=info["numero"], valor=info["valor"], fecha=info["fecha"])
            ven.save()
            return render(request, "AppMiEmprendimiento/index.html")
    else:
        miFormulario = VentaFormulario()
 
    return render(request, "AppMiEmprendimiento/ventas_alta.html", {"miFormulario": miFormulario})

def buscar_ventas(request):
    if request.method == "POST":
        miFormulario = BuscarVentaFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            ventas = Venta.objects.filter(fecha__icontains=info["fecha"])
            return render(request, "AppMiEmprendimiento/ventas_resultados.html", {"ventas": ventas})
    else:
        miFormulario = BuscarVentaFormulario()
 
    return render(request, "AppMiEmprendimiento/ventas_buscar.html", {"miFormulario": miFormulario})