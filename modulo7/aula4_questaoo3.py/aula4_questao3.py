
import re
import os
import requests

# URL do arquivo
url = "https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt"

# Obtém o diretório atual do script
dir_path = os.path.abspath(os.path.dirname(__file__))

# Caminho completo para o arquivo "estomago.txt"
file_path = os.path.join(dir_path, "estomago.txt")

# Baixa o arquivo
response = requests.get(url)
with open(file_path, "wb") as file:
    file.write(response.content)

print(f"Arquivo 'estomago.txt' baixado e salvo em {file_path}")

# Verifica se o arquivo existe
if not os.path.exists(file_path):
    print("Arquivo 'estomago.txt' não encontrado.")
else:
    # Lê o arquivo
    with open(file_path, "r", encoding="utf-8") as file:
        linhas = file.readlines()

    # Imprime as primeiras 25 linhas
    print("Texto das primeiras 25 linhas:")
    for linha in linhas[:25]:
        print(linha.strip())

    # Número de linhas
    num_linhas = len(linhas)
    print(f"\nNúmero de linhas do arquivo: {num_linhas}")

    # Linha com maior número de caracteres
    linha_maior = max(linhas, key=len)
    print(f"\nLinha com maior número de caracteres: {linha_maior.strip()}")

    # Menções aos personagens "Nonato" e "Íria"
    mentions_nonato = sum(1 for linha in linhas if re.search(r'\bNonato\b', linha, re.IGNORECASE))
    mentions_iria = sum(1 for linha in linhas if re.search(r'\bÍria\b', linha, re.IGNORECASE))

    print(f"\nMenções de 'Nonato': {mentions_nonato}")
    print
