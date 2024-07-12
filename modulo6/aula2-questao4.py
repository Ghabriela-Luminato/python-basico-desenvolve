
def intercala_listas(lista1, lista2):
    intercalada = []
    for l1, l2 in zip(lista1, lista2):
        intercalada.append(l1)
        intercalada.append(l2)
    intercalada.extend(lista1[len(lista2):] or lista2[len(lista1):])
    return intercalada


quantidade_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {quantidade_lista1} elementos da lista 1:")
lista1 = [int(input()) for _ in range(quantidade_lista1)]

quantidade_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {quantidade_lista2} elementos da lista 2:")
lista2 = [int(input()) for _ in range(quantidade_lista2)]

lista_intercalada = intercala_listas(lista1, lista2)

print(f"Lista intercalada: {' '.join(map(str, lista_intercalada))}")
