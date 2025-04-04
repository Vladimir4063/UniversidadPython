class ClaseBase:
    def __init__(self):
        print("Constructor de ClaseBase")

    def metodo_clase(self):
        print("Metodo de la clase base")

class ClaseDerivada(ClaseBase):
    def __init__(self):
        print("Constructor de ClaseDerivada")
    # Si el constructor de la ClaseDerivada no existe, tomara 
    # el constructor de la clase base.

    #Si nombre del metodo se repite, tomara el nuevo metodo construido

obj = ClaseDerivada()

obj.metodo_clase()