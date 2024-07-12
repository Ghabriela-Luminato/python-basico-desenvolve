import os

# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Obtém o diretório atual do script
dir_path = os.path.abspath(os.path.dirname(__file__))

# Caminho completo para o arquivo "frase.txt"
file_path = os.path.join(dir_path, "frase.txt")

# Salva a frase no arquivo "frase.txt"
with open(file_path, "w", encoding="utf-8") as file:
    file.write(frase)

# Imprime o caminho completo do arquivo salvo
print(f"Frase salva em {file_path}")

