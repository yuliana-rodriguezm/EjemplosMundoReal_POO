# Representa a un cliente de la pastelería

class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"Cliente({self.nombre})"
