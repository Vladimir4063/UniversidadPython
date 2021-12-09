#Creamos una tupla
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres('Vladii', 'Ivan', 'Adelina')
listarNombres('Laura', 'Guillermo')


#Suma de elementos
def sumarPersonas(*cantidad) -> int:
    total = 0
    for persona in cantidad:
        total = total +1
    return total

print("Cantidad de personas: " + str(sumarPersonas('Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto')))

#Suma de valores
def sumarValores(*valor) -> int:
    sumaTotal = 0
    for valores in valor:
        sumaTotal = sumaTotal + valores
    return sumaTotal

print("Suma total de valores: " + str(sumarValores(23,23,12,45,64)))