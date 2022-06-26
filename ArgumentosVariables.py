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

def multiplicaValores(*valor) -> int:
    sumaTotalMulti = 0
    for valores in valor:
        sumaTotalMulti= valores * valor[0]
        print(sumaTotalMulti)

print("Ingrese el primer parametro como numero multiplo. Apartir del segundo parametro, seran numeros a multiplicar por el primero")
multiplicaValores(3, 2, 4, 2, 1, 2)