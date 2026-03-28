from django.db import models

# Create your models here.
class Pedido(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha y hora en que se creó el pedido, se establece automáticamente al crear un nuevo pedido
    total = models.FloatField()  # Total del pedido, se almacena como un número de punto flotante