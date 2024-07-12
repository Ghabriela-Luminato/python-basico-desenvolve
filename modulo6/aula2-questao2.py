

import random


num_elementos = random.randint(5, 20)


elementos = [random.randint(1, 10) for _ in range(num_elementos)]


soma_valores = sum(elementos)
media_valores = soma_valores / num_elementos


print(f"Lista de elementos: {elementos}")
print(f"Soma dos valores: {soma_valores}")
print(f"Média dos valores: {media_valores:.2f}")
