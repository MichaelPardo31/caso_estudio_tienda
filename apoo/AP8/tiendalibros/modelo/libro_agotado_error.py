from tiendalibros.modelo.libro_error import LibroError



class LibroAgotadoError(LibroError):
    def __init__(self, isbn, titulo):
        super().__init__(f"El libro con titulo {titulo} y isbn {isbn} está agotado")


