from django.urls import path
from AppMiEmprendimiento  import views

urlpatterns = [
    path('inicio/', views.inicio),
    path('proveedores/', views.proveedores, name="Proveedores"),
    path('pedidos/', views.pedidos, name="Pedidos"),
    path('clientes/', views.clientes, name="Clientes"),
    path('ventas/', views.ventas, name="Ventas")
]
