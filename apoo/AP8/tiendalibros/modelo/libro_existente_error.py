from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):

    # Defina metodo inicializador
    def __init__(self, libro):
        pass

    # Defina metodo especial
    def __str__(self):
        return f"El libro con titulo <TITULO_DEL_LIRBO> y isbn: <ISBN_DEL_LIBRO> ya existe en el catálogo"


