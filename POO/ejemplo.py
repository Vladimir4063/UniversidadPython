class Perro:
    especie = "Canis lupus familiaria"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("Se ejecuto el constructor")
    def ladrar(self):
        print("Guau guau!!")

mi_perro = Perro("Rocky", 3)
print(mi_perro.nombre)
print(mi_perro.edad)
mi_perro.ladrar()
