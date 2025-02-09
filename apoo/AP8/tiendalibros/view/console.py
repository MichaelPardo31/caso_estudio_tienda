import sys

from tiendalibros.modelo.tienda_libros import TiendaLibros


class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    def retirar_libro_de_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro que desea retirar: ")
        self.tienda.retirar_item_de_carrito(isbn)
        print("Libro retirado exitosamente del carrito.")

    def agregar_libro_a_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro que desea agregar: ")
        cantidad = int(input("Ingrese la cantidad de unidades: "))
        try:
            self.tienda.agregar_libro_a_carrito(isbn, cantidad)
            print(f"{cantidad} unidades del libro con ISBN {isbn} fueron añadidas al carrito.")
        except LibroError as e:
            print(f"Error: {str(e)}")

    def adicionar_un_libro_a_catalogo(self):
        isbn = input("Ingrese el ISBN: ")
        titulo = input("Ingrese el titulo: ")
        precio = float(input("Ingrese el precio: "))
        existencias = int(input("Ingrese las existencias: "))
        try:
            self.tienda.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print(f"El libro '{titulo}' fue añadido al catálogo exitosamente.")
        except LibroError as e:
            print(f"Error: {str(e)}")
