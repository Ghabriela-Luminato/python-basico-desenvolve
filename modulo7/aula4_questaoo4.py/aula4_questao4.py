import random
import os

# Obtém o diretório atual do script
dir_path = os.path.abspath(os.path.dirname(__file__))

# Abrir o arquivo gabarito_forca.txt e escolher uma palavra aleatória
with open(os.path.join(dir_path, "gabarito_forca.txt"), "r", encoding="utf-8") as file:
    words = file.readlines()

# Escolher uma palavra aleatória e remover espaços em branco
chosen_word = random.choice(words).strip().lower()

# Criar a lista de estágios do enforcado a partir do gabarito_enforcado.txt
with open(os.path.join(dir_path, "gabarito_enforcado.txt"), "r", encoding="utf-8") as file:
    stages = file.readlines()

# Limite de tentativas
max_attempts = 6
attempts = 0

# Palavra oculta inicialmente como underscores
hidden_word = "_" * len(chosen_word)

# Conjunto para armazenar letras já tentadas
used_letters = set()

# Função para imprimir o enforcado conforme o número de erros
def print_hangman(errors):
    for line in stages[0:errors + 1]:
        print(line.rstrip())

# Jogo principal
print(f"Bem-vindo ao Jogo da Forca! Adivinhe a palavra de {len(chosen_word)} letras.")

while attempts < max_attempts:
    print("\nPalavra:", " ".join(hidden_word))

    guess = input("Digite uma letra: ").strip().lower()

    if guess in used_letters:
        print("Você já tentou essa letra. Tente outra.")
        continue
    else:
        used_letters.add(guess)

    if guess in chosen_word:
        # Atualizar a palavra oculta com as letras corretamente adivinhadas
        temp_word = list(hidden_word)
        indices = [i for i, letter in enumerate(chosen_word) if letter == guess]
        for index in indices:
            temp_word[index] = guess
        hidden_word = "".join(temp_word)

        # Verificar se o jogador venceu
        if "_" not in hidden_word:
            print(f"\nParabéns! Você acertou a palavra '{chosen_word}'.")
            break
    else:
        print("\nLetra incorreta.")
        attempts += 1
        print_hangman(attempts)

# Verificar se o jogador perdeu
if attempts == max_attempts:
    print(f"\nVocê perdeu! A palavra era '{chosen_word}'.")
