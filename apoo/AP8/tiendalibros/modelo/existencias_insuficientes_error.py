from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    def __init__(self, isbn, titulo, cantidad_a_comprar, existencias):
        super().__init__(f"El libro con titulo {titulo} y isbn {isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {cantidad_a_comprar}, existencias: {existencias}")
        self.cantidad_a_comprar = cantidad_a_comprar
