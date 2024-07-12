import os
import re

# Diretório onde o script está localizado
dir_path = os.path.dirname(os.path.abspath(__file__))

# Caminho completo para o arquivo "frase.txt"
input_file_path = os.path.join(dir_path, "frase.txt")

# Caminho completo para o arquivo "palavras.txt"
output_file_path = os.path.join(dir_path, "palavras.txt")

# Lê o arquivo salvo
with open(input_file_path, "r", encoding="utf-8") as input_file:
    texto = input_file.read()

# Remove espaços em branco e caracteres não alfabéticos, separando cada palavra em uma linha
palavras = re.findall(r'\b[a-zA-Z]+\b', texto)

# Salva as palavras no arquivo "palavras.txt"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    for palavra in palavras:
        output_file.write(palavra + "\n")

print(f"Palavras salvas em {output_file_path}")
