
distancia = float(input("Digite a distância da entrega em quilômetros: "))
peso = float(input("Digite o peso do pacote em quilogramas: "))


if peso > 10:
    taxa_adicional = 10
else:
    taxa_adicional = 0

if distancia <= 100:
    valor_frete = peso * 1
elif distancia <= 300:
    valor_frete = peso * 1.5
else:
    valor_frete = peso * 2

# Calcula o valor total do frete
valor_total = valor_frete + taxa_adicional

# Imprime o valor total do frete
print(f"O valor total do frete é R${valor_total:.2f}")
