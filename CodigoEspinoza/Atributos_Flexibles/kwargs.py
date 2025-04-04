def mostrar_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}:{valor}")

mostrar_informacion(nombre="Ana", edad=25, ciudad="Madrid")
# Debo entregar los argumentos con clave:valor