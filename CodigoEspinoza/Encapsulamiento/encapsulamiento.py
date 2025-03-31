class Auto:
    def __init__(self, marca, modelo, anio):
        self.__marca = marca
        self.__modelo = modelo
        self.anio = anio

    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def set_marca(self, marca):
        self.__marca = marca

    # metodo privado
    def __acelerar(self):
        print("Acelerando..")
    
mi_auto = Auto("Citroen", "C4", 2016)

print(mi_auto.anio)
# print(mi_auto.get_marca())
print(f"Hola, esta marca es {mi_auto.get_marca()} y el modelo es {mi_auto.get_modelo()}")

mi_auto.set_marca("Audi")
print(f"Hola, esta marca es {mi_auto.get_marca()} y el modelo es {mi_auto.get_modelo()}")


#Acceder a un metodo privado
mi_auto._Auto__acelerar()
