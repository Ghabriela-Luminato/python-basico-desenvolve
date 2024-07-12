
numeros = []
print("Digite pelo menos 4 números inteiros. Para parar, digite 'sair':")
while True:
    entrada = input()
    if entrada.lower() == 'sair':
        if len(numeros) >= 4:
            break
        else:
            print("Digite pelo menos 4 números.")
    else:
        try:
            numeros.append(int(entrada))
        except ValueError:
            print("Por favor, digite um número inteiro ou 'sair'.")

print(f"Lista original: {numeros}")
print(f"Os 3 primeiros elementos: {numeros[:3]}")
print(f"Os 2 últimos elementos: {numeros[-2:]}")
print(f"A lista invertida: {numeros[::-1]}")
print(f"Os elementos de índice par: {numeros[::2]}")
print(f"Os elementos de índice ímpar: {numeros[1::2]}")
