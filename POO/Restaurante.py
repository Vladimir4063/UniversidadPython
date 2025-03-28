
"""
Supuestos
1) Los items tiene nombre y precio, ejemplo : {"hamburguesa":3.5}
2) Las mesas estaran enumeradas, tendran un nombre de la persona que reservo el estado de la mesa (si esta reservada o no)
3) Las ordenes tendran el nombre del cliente y los items deseados
"""

class Restaurant:
    def __init__(self, ):
        self.menu = {}
        self.mesas = {}
        self.mesas_reservadas = {}
        self.ordenes = {}

    def add_item(self, item, precio):
        self.menu[item] = precio

    def reserva_mesas(self, numero, nombre_cliente):
        if numero not in self.mesas_reservadas:
            self.mesas_reservadas[numero] = nombre_cliente
        else:
            print(f"Lo siento la mesa {numero} está reservada")

    def pedidos(self, numero, items):
        if numero not in self.ordenes:
            self.ordenes[numero] = items
        else:
            self.ordenes[numero].append(items)
            
    def imprimir_menu(self):
        print(self.menu)

    def imprimir_reservas(self):
        print(self.mesas_reservadas)
    
    def imprimir_pedidos(self):
        print(self.ordenes)

restaurante = Restaurant()
restaurante.add_item("Hamburguesa", 3.5)
restaurante.add_item("Completo", 4)
restaurante.reserva_mesas(1,"Ivan")
restaurante.reserva_mesas(2,"Juanita")
# restaurante.reserva_mesas(2,"Ivan")
restaurante.pedidos(1, ["Hamburguesas", "Completos"])
restaurante.pedidos(1, "Hambur simple")

restaurante.imprimir_menu()
restaurante.imprimir_reservas()
restaurante.imprimir_pedidos()