

import random

lista = [random.randint(1, 100) for _ in range(20)]

while True:
    tamanho = int(input("Tamanho para divisão: "))
    if tamanho == 0:
        break
    sublistas = [lista[i:i + tamanho] for i in range(0, len(lista), tamanho)]
    print("Sublistas:", sublistas)
