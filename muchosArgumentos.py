import pstats


def sumar_muchosValores(*args):
    resultado = 0

    for valor in args:
        resultado += valor
    return resultado

print(sumar_muchosValores(1,2,3,4))