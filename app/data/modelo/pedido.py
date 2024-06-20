class Pedido:
    def __init__(self, id_pedido : int,fecha : str, articulo:str,cantidad:str,precio_unidad:str,precio_total,id_cliente:int):
        self.id_pedido = id_pedido
        self.fecha = fecha
        self.articulo = articulo
        self.cantidad = cantidad
        self.precio_unidad = precio_unidad
        self.precio_total = precio_total
        self.id_cliente = id_cliente