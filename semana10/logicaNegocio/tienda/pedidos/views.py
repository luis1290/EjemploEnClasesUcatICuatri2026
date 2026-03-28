from django.shortcuts import render
from django.http import JsonResponse
from .services.pedido_service import (
    PedidoService,
)  # Importamos la clase PedidoService desde el módulo services para poder utilizar sus métodos en nuestras vistas

# librerias de Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer


# Create your views here.
@api_view(["POST"])  # Decorador que indica que esta vista solo acepta solicitudes POST, lo que significa que se espera que el cliente envíe datos para crear un nuevo pedido
def crear_pedido(request):
    serializer = ItemSerializer(data=request.data, many=True)

    if (
        serializer.is_valid()
    ):  # Verificamos si los datos enviados por el cliente son válidos según las reglas definidas en el serializador ItemSerializer
        items = serializer.validated_data
        pedido = PedidoService.crear_pedido(items)
        return Response(
            {"id": pedido.id, "fecha": pedido.fecha, "total": pedido.total},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def obtener_pedidos(request):
    pedidos = PedidoService.obtener_pedido()
    data = [
        {"id": p.id, "fecha": p.fecha, "total": p.total} for p in pedidos
    ]  # Creamos una lista de diccionarios con los datos de cada pedido, donde cada diccionario contiene el id, la fecha y el total del pedido
    return Response(
        data, status=status.HTTP_200_OK
    )  # Retornamos la lista de pedidos en formato JSON con un código de estado HTTP 200 OK
