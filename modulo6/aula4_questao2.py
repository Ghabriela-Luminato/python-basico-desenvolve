
frase = input("Digite uma frase: ")


vogais = sorted([char for char in frase if char.lower() in 'aeiou'])
consoantes = [char for char in frase if char.isalpha() and char.lower() not in 'aeiou']

print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")
