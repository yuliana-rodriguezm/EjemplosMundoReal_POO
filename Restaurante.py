# Caso del mundo real:
# Un puesto de comida rápida muestra su menú

# Clase que representa un producto de comida rápida
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_producto(self):
        print(f"{self.nombre} - ${self.precio}")

# Clase que representa el menú del local
class Menu:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_menu(self):
        print("\nMenú:")
        for producto in self.productos:
            producto.mostrar_producto()

# Clase que representa el puesto de comida rápida
class ComidaRapida:
    def __init__(self, nombre):
        self.nombre = nombre
        self.menu = Menu()

    def mostrar_comida_rapida(self):
        print(f"Comida Rápida: {self.nombre}")
        self.menu.mostrar_menu()


# Creación del local
local = ComidaRapida("El Rincón del Sabor")

# Crea los de productos
hamburguesa = Producto("Hamburguesa", 3.00)
pizza = Producto("Pizza personal + vaso de cola", 1.50)
hotdog = Producto("Hot Dog", 2.75)
salchipapa = Producto("Salchipapa", 2.00)
papipollo = Producto("PapiPollo", 3.50)
cocacola = Producto("CocaCola personal", 0.50)

# Agrega productos al menú
local.menu.agregar_producto(hamburguesa)
local.menu.agregar_producto(pizza)
local.menu.agregar_producto(hotdog)
local.menu.agregar_producto(salchipapa)
local.menu.agregar_producto(papipollo)
local.menu.agregar_producto(cocacola)

# Mostra todo el menú
local.mostrar_comida_rapida()
