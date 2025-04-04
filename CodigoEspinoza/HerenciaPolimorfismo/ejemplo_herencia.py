# Clase principal
class Animal:
    def __init__(self, nombre:str):
        self.nombre = nombre

    def hablar(self):
        print("se llamo al metodo hablar")

# Clase derivada
class Perro(Animal):
    def hablar(self):
        return "Guau!"
    

class Gato(Animal):
    def hablar(self):
        super().hablar()
        return "Miau!"
    
mi_perro = Perro(nombre="Rocky")
mi_gato = Gato(nombre="Luna")

print(mi_perro.hablar())
print(mi_gato.hablar())

print(mi_perro.nombre) #Rocky
print(mi_gato.nombre) #Luna