from pedidos.models import Pedido  # Importamos el modelo Pedido desde el módulo models para poder interactuar con la base de datos y crear nuevos pedidos

class PedidoService:

    def calcularTotal(items):
        total = sum([i['precio'] * i['cantidad'] for i in items])  # Calcula el total sumando el precio multiplicado por la cantidad de cada ítem en la lista de ítems
        if total > 100:  # Si el total es mayor a 100, se aplica un descuento del 10%
            total *= 0.9  # Aplica el descuento multiplicando el total por 0.9 (equivalente a restar el 10%)
        return total  # Retorna el total calculado, ya sea con o sin descuento
    
    def crear_pedido(items):
        total = PedidoService.calcularTotal(items)
        pedido = Pedido.objects.create(total=total)  # Crea un nuevo pedido en la base de datos con el total calculado
        return pedido  # Retorna el pedido creado
    
    def obtener_pedido():
        return Pedido.objects.all()