# Caso del mundo real:
# Una pastelería gestiona la venta de pasteles

class Pastel:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.vendido = False

    def vender(self):
        if self.vendido:
            return False
        self.vendido = True
        return True

    def devolver(self):
        if not self.vendido:
            return False
        self.vendido = False
        return True

    def __str__(self):
        estado = "Vendido" if self.vendido else "Disponible"
        return f"Pastel({self.nombre}, {estado})"
