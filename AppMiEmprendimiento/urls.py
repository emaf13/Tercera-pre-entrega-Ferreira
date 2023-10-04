from django.urls import path
from AppMiEmprendimiento  import views

urlpatterns = [
    path('inicio/', views.inicio),
    path('proveedores/', views.proveedores),
    path('pedidos/', views.pedidos),
    path('clientes/', views.clientes),
    path('ventas/', views.ventas)
]
