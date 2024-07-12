
import csv
import os

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

# Obtém o diretório atual do script
dir_path = os.path.abspath(os.path.dirname(__file__))

# Caminho completo para o arquivo CSV de saída
csv_file_path = os.path.join(dir_path, "meus_livros.csv")

# Cria e escreve no arquivo CSV
with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
    # Define o cabeçalho
    fieldnames = ["Título", "Autor", "Ano de publicação", "Número de páginas"]
    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Escreve o cabeçalho
    writer.writeheader()
    
    # Escreve os dados dos livros
    for livro in livros:
        writer.writerow(livro)

print(f"Arquivo CSV 'meus_livros.csv' criado em {csv_file_path}")
