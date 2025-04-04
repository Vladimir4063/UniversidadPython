def crear_persona(*args, **kwargs):
    nombre, apellido = args
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")

    for k, v in kwargs.items():
        print(f"{k}:{v}")

crear_persona("Juan", "Perez", edad=28, ciudad="Valencia")
# Combinacion de ambos metodos, unir listas y diccionarios(k:v)