
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").lower()
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))


if classe == 'guerreiro':
    pontos_consistentes = forca >= 15 and magia <= 10
elif classe == 'mago':
    pontos_consistentes = forca <= 10 and magia >= 15
elif classe == 'arqueiro':
    pontos_consistentes = forca > 5 and forca <= 15 and magia > 5 and magia <= 15
else:
    pontos_consistentes = False


print("Pontos de atributo consistentes com a classe escolhida:", pontos_consistentes)
