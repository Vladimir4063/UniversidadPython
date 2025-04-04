# Clase principal
class Animal:
    def hablar(self):
        pass

# Clase derivada
class Perro(Animal):
    def hablar(self):
        return "Guau!"
    

class Gato(Animal):
    def hablar(self):
        return "Miau!"
 
# Polimorfismo: El opbjeto es el parametro a entregar. 
# Dependiendo eso, devuelve el metodo
def escuchar_animal(animal):
    print(animal.hablar())

perro = Perro()
gato = Gato()

escuchar_animal(perro)
escuchar_animal(gato)