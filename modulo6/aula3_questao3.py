

import random


lista = [random.randint(-10, 10) for _ in range(20)]


print(f"Lista original: {lista}")


max_negativos = 0
intervalo = (0, 0)

for i in range(len(lista)):
    for j in range(i + 1, len(lista) + 1):
        sub_lista = lista[i:j]
        num_negativos = sum(1 for x in sub_lista if x < 0)
        if num_negativos > max_negativos:
            max_negativos = num_negativos
            intervalo = (i, j)


del lista[intervalo[0]:intervalo[1]]


print(f"Lista editada: {lista}")
