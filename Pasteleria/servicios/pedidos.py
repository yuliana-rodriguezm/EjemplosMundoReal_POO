# Servicio que gestiona los pedidos de la pastelería

from modelos.pastel import Pastel
from modelos.cliente import Cliente


class Pedido:
    def __init__(self):
        self.pasteles = []

    def agregar_pastel(self, pastel: Pastel):
        self.pasteles.append(pastel)

    def vender_pastel(self, nombre_pastel: str, cliente: Cliente):
        for pastel in self.pasteles:
            if pastel.nombre == nombre_pastel:
                if pastel.vender():
                    return f"Pastel vendido a {cliente.nombre}"
                else:
                    return "El pastel ya fue vendido"
        return "Pastel no encontrado"
