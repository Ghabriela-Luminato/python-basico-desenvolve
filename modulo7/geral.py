import os

# Função para criar diretório e arquivo
def create_directory_and_file(directory, filename, content=""):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    return file_path

# Diretório base para todas as questões
base_dir = "c:/python/modulo7/"

# Questão 1
questao1_dir = os.path.join(base_dir, "aula4_questao1")
questao1_file = "aula4_questao1.py"
questao1_content = '''# aula4_questao1.py
import os

# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Caminho para salvar o arquivo
file_path = "C:/python/modulo7/aula4_questao1/frase.txt"

# Salva a frase no arquivo
with open(file_path, "w", encoding="utf-8") as file:
    file.write(frase)

# Imprime o caminho completo do arquivo salvo
print(f"Frase salva em {file_path}")
'''
create_directory_and_file(questao1_dir, questao1_file, questao1_content)

# Questão 2
questao2_dir = os.path.join(base_dir, "aula4_questao2")
questao2_file = "aula4_questao2.py"
questao2_content = '''# aula4_questao2.py
import re

# Caminho do arquivo com a frase
file_path = "C:/python/modulo7/aula4_questao1/frase.txt"

# Caminho para salvar o arquivo com as palavras
output_path = "C:/python/modulo7/aula4_questao2/palavras.txt"

# Lê a frase do arquivo
with open(file_path, "r", encoding="utf-8") as file:
    frase = file.read()

# Remove caracteres não alfabéticos e separa as palavras
palavras = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ]+", frase)

# Salva as palavras no arquivo
with open(output_path, "w", encoding="utf-8") as output_file:
    for palavra in palavras:
        output_file.write(palavra + "\\n")

# Imprime o conteúdo do arquivo
with open(output_path, "r", encoding="utf-8") as output_file:
    print(output_file.read())
'''
create_directory_and_file(questao2_dir, questao2_file, questao2_content)

# Questão 3
questao3_dir = os.path.join(base_dir, "aula4_questao3")
questao3_file = "aula4_questao3.py"
questao3_content = '''# aula4_questao3.py
import re

# Caminho do arquivo
file_path = "C:/python/modulo7/aula4_questao3/estomago.txt"

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
    print(f"\\nNúmero de linhas do arquivo: {num_linhas}")

    # Linha com maior número de caracteres
    linha_maior = max(linhas, key=len)
    print(f"\\nLinha com maior número de caracteres: {linha_maior.strip()}")

    # Menções aos personagens "Nonato" e "Íria"
    mentions_nonato = sum(1 for linha in linhas if re.search(r'\\bNonato\\b', linha, re.IGNORECASE))
    mentions_iria = sum(1 for linha in linhas if re.search(r'\\bÍria\\b', linha, re.IGNORECASE))

    print(f"\\nMenções de 'Nonato': {mentions_nonato}")
    print(f"Menções de 'Íria': {mentions_iria}")
'''
create_directory_and_file(questao3_dir, questao3_file, questao3_content)

# Questão 4
questao4_dir = os.path.join(base_dir, "aula4_questao4")
questao4_file = "aula4_questao4.py"
questao4_content = '''# aula4_questao4.py
import random

# Função para imprimir o enforcado
def imprime_enforcado(erros):
    estagios = [
        "",
        " O ",
        " O \n | ",
        " O \n/| ",
        " O \n/|\\",
        " O \n/|\\ \n/  ",
        " O \n/|\\ \n/ \\"
    ]
    print(estagios[erros])

# Caminho dos arquivos
gabarito_forca = "C:/python/modulo7/aula4_questao4/gabarito_forca.txt"
gabarito_enforcado = "C:/python/modulo7/aula4_questao4/gabarito_enforcado.txt"

# Lê o arquivo de palavras
with open(gabarito_forca, "r", encoding="utf-8") as file:
    palavras = file.read().splitlines()

# Escolhe uma palavra aleatória
palavra = random.choice(palavras)
tentativas = 6
letras_acertadas = ["_" for _ in palavra]
erros = 0

print("Palavra:", " ".join(letras_acertadas))

while erros < tentativas and "_" in letras_acertadas:
    letra = input("Digite uma letra: ").lower()

    if letra in palavra:
        for index, char in enumerate(palavra):
            if char == letra:
                letras_acertadas[index] = letra
    else:
        erros += 1
        imprime_enforcado(erros)

    print("Palavra:", " ".join(letras_acertadas))

if "_" not in letras_acertadas:
    print("Parabéns, você acertou a palavra!")
else:
    print(f"Você perdeu! A palavra era: {palavra}")
'''
create_directory_and_file(questao4_dir, questao4_file, questao4_content)

# Questão 5
questao5_dir = os.path.join(base_dir, "aula4_questao5")
questao5_file = "aula4_questao5.py"
questao5_content = '''# aula4_questao5.py
import csv

# Lista de livros
livros = [
    {"Título": "Dom Casmurro", "Autor": "Machado de Assis", "Ano de publicação": 1899, "Número de páginas": 256},
    {"Título": "1984", "Autor": "George Orwell", "Ano de publicação": 1949, "Número de páginas": 328},
    {"Título": "Harry Potter e a Pedra Filosofal", "Autor": "J.K. Rowling", "Ano de publicação": 1997, "Número de páginas": 309},
    {"Título": "A Metamorfose", "Autor": "Franz Kafka", "Ano de publicação": 1915, "Número de páginas": 102},
    {"Título": "Crime e Castigo", "Autor": "Fiódor Dostoiévski", "Ano de publicação": 1866, "Número de páginas": 551},
    {"Título": "A Revolução dos Bichos", "Autor": "George Orwell", "Ano de publicação": 1945, "Número de páginas": 160},
    {"Título": "O Hobbit", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1937, "Número de páginas": 310},
    {"Título": "O Pequeno Príncipe", "Autor": "Antoine de Saint-Exupéry", "Ano de publicação": 1943, "Número de páginas": 96},
    {"Título": "O Senhor dos Anéis: A Sociedade do Anel", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1954, "Número de páginas": 576},
    {"Título": "A Guerra dos Tronos", "Autor": "George R.R. Martin", "Ano de publicação": 1996, "Número de páginas": 800}
]

# Caminho do arquivo CSV
csv_file_path = "C:/python/modulo7/aula4_questao5/meus_livros.csv"

# Cria e escreve no arquivo CSV
with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Título", "Autor", "Ano de publicação", "Número de páginas"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for livro in livros:
        writer.writerow(livro)

print(f"Arquivo CSV 'meus_livros.csv' criado em {csv_file_path}")
'''
create_directory_and_file(questao5_dir, questao5_file, questao5_content)

# Questão 6
questao6_dir = os.path.join(base_dir, "aula4_questao6")
questao6_file = "aula4_questao6.py"
questao6_content = '''# aula4_questao6.py
import csv

# Caminho do arquivo CSV de músicas do Spotify
csv_file_path = "C:/python/modulo7/aula4_questao6/spotify_musicas.csv"

# Leitura do arquivo CSV
with open(csv_file_path, "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    # Lista de dicionários contendo as informações de cada música
    musicas = [row for row in reader]

# Imprime as informações de cada música
for musica in musicas:
    print(f"Título: {musica['Título']}")
    print(f"Artista: {musica['Artista']}")
    print(f"Álbum: {musica['Álbum']}")
    print(f"Duração: {musica['Duração']}")
    print(f"Ano de lançamento: {musica['Ano de lançamento']}")
    print()
'''
create_directory_and_file(questao6_dir, questao6_file, questao6_content)
