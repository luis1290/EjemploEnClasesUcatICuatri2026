from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),  # Ruta para crear un nuevo pedido, se asigna a la vista crear_pedido y se le da el nombre 'crear_pedido' para poder referenciarla fácilmente en otras partes del código
    path("api/crear/", views.crear_pedido, name="crear_pedido"),
    path("api/pedidos/", views.obtener_pedidos, name="obtener_pedidos"), 
]
