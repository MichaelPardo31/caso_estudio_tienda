from libro import Libro
from carro_compra import CarroCompras

class TiendaLibros:
    # Defina metodo inicializador __init__
    def __init__(self):
        self.catalogo: dict[str, Libro] = {}
        carrito = CarroCompras()

        

    def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int):
        if isbn in self.catalogo:
            raise LibroExistenteError(isbn, titulo)
        libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = libro
        return libro

    # Defina metodo agregar_libro_a_carrito
    def agregar_libro_a_carrito(self, isbn: str, cantidad: int):
        libro = self.catalogo.get(isbn)
        if libro is None:
            raise LibroAgotadoError(isbn, libro.titulo)

        if libro.existencias < cantidad:
            raise ExistenciasInsuficientesError(isbn, libro.titulo, cantidad, libro.existencias)

        libro.existencias -= cantidad
        return self.carrito.agregar_item(libro, cantidad)

    def retirar_item_de_carrito(self, isbn: str):
        self.carrito.quitar_item(isbn)
