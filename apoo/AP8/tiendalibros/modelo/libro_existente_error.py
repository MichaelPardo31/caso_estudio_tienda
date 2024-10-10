from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):

    # Defina metodo inicializador
    def __init__(self, isbn, titulo):
        super().__init__(f"El libro con titulo {titulo} y isbn {isbn} ya existe en el catálogo")



