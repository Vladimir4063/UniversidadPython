def multiplicar_numeros(a,b,c):
    return a*b*c

numeros = (2,3,4)
resultado = multiplicar_numeros(*numeros) #Envio argumentos agrupados
print(resultado)


def mostrar_informacion(nombre, edad, ciudad):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")

# Enviamos los valores agrupados en Clave:Valor  
info = {"nombre":"Carlos", "edad":30, "ciudad":"Pinamar"}
mostrar_informacion(**info)