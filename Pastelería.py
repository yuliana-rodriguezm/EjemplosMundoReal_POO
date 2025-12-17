# Caso del mundo real:
# Una pastelería vende pasteles y recibe pedidos de clientes

# Clase que representa un pastel de la pastelería
class Pastel:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # Muestra la información del pastel
    def mostrar_info(self):
        print(f"Pastel: {self.nombre} - Precio: ${self.precio}")


# Clase que representa a un cliente de la pastelería
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre


# Clase que representa un pedido realizado por un cliente
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.pasteles = []

    # Agrega un pastel al pedido del cliente
    def agregar_pastel(self, pastel):
        self.pasteles.append(pastel)
        print(f"{pastel.nombre} agregado al pedido")

    # Calcula el total a pagar del pedido
    def calcular_total(self):
        total = 0
        for pastel in self.pasteles:
            total += pastel.precio
        return total

    def mostrar_pedido(self):
        print(f"\nPedido del cliente: {self.cliente.nombre}")
        for pastel in self.pasteles:
            print(f"- {pastel.nombre} (${pastel.precio})")
        print(f"Total a pagar: ${self.calcular_total()}")

# Creación de pasteles personalizados por los clientes
pastel1 = Pastel("Pastel de Chocolate", 15)
pastel2 = Pastel("Pastel de Cafe + decoraciones", 18)
pastel3 = Pastel("Pastel tres leches", 20)
pastel4 = Pastel("Pastel con relleno de mermelada de fresa", 14)

# Creación de clientes
cliente1 = Cliente("Mercedes Vera")
cliente2 = Cliente("Joss Duglas")

# Pedido 1
pedido1 = Pedido(cliente1)
pedido1.agregar_pastel(pastel1)
pedido1.agregar_pastel(pastel2)

# Pedido 2
pedido2 = Pedido(cliente2)
pedido2.agregar_pastel(pastel3)
pedido2.agregar_pastel(pastel4)

# Muestra los pedidos realizados
pedido1.mostrar_pedido()
pedido2.mostrar_pedido()