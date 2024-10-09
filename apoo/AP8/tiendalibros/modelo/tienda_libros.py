from libro import Libro
from carro_compra import CarroCompras
class TiendaLibros:
    # Defina metodo inicializador __init__
    def __init__(self):
        self.catalogo: dict[str, Libro] = {}
        carrito = CarroCompras()

        

    def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int):
        self.isbn = isbn
        self.titulo = titulo
        self.precio = precio
        self.existencias = existencias
        
        return 

    # Defina metodo agregar_libro_a_carrito

    # Defina metodo retirar_item_de_carrito
