def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

resultado = sumar_numeros(1,2,3,4,5,7)
print(resultado)
#Si quiere usar un número indefinido de argumentos
