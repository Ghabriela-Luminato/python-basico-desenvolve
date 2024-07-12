

import random


valores = [random.randint(-100, 100) for _ in range(20)]


lista_ordenada = sorted(valores)


indice_maior = valores.index(max(valores))


indice_menor = valores.index(min(valores))

print(f"Lista ordenada: {lista_ordenada}")
print(f"Lista original: {valores}")
print(f"Índice do maior valor: {indice_maior}")
print(f"Índice do menor valor: {indice_menor}")
