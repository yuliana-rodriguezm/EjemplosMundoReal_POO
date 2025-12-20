# Programa principal de la pastelería

from modelos.pastel import Pastel
from modelos.cliente import Cliente
from servicios.pedidos import Pedido

pedido = Pedido()

pastel1 = Pastel("Pastel de Chocolate", 15)
pastel2 = Pastel("Pastel de Moca", 18)

cliente = Cliente("Mercedes Vera", "0102030405")

pedido.agregar_pastel(pastel1)
pedido.agregar_pastel(pastel2)

print(pedido.vender_pastel("Pastel de Chocolate", cliente))
print(pastel1)
print(pastel2)
