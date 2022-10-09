from functools import reduce


def suma(a, b):
    return a + b


lista = [1, 3, 6, 8, 45, 44, 32, 15, 19]

lista2 = list(filter(lambda x: x % 2 != 0, lista))

print(list(lista2))





resul = reduce(suma, lista2)

print(resul)
