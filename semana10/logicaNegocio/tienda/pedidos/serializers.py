from rest_framework import serializers # Importamos el módulo serializers de Django REST Framework para poder crear serializadores que nos permitan convertir nuestros modelos a formatos como JSON y viceversa

class ItemSerializer(serializers.Serializer):
    precio = serializers.FloatField()  # Definimos un campo de tipo Float para el precio del ítem
    cantidad = serializers.IntegerField()  # Definimos un campo de tipo Integer para la cantidad del ítem