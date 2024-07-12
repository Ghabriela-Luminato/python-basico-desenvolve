
def diferenca_listas(lista1, lista2):
    lista_dif = lista1[:]
    for elem in lista2:
        if elem in lista_dif:
            lista_dif.remove(elem)
    return lista_dif

lista1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
lista2 = [1, 1, 2, 4, 5, 6]
resultado = diferenca_listas(lista1, lista2)
print("Diferença entre as listas:", resultado)
