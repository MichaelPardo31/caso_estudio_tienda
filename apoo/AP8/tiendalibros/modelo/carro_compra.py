from item_compra import ItemCompra

class CarroCompras:
    # Defina metodo inicializador __init__(self)
    def __init__(self):
        self.item: list[ItemCompra] = []

    # Defina el metodo agregar_item
    def agregar_item(self, libro, cantidad: int):
        objeto = ItemCompra(libro, cantidad)
        self.item.append(objeto)
        return objeto

    # Defina el metodo calcular_total
    def calcular_total(self):
        total = sum(self.item.calcular_subtotal() for self.item in self.items)
        return total
        
    # Defina el metodo quitar_item
    def quitar_item(self, isbn):
        self.item = [x for x in self.item if x.libro.isbn != isbn]
