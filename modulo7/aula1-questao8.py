

def avalia_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            return linha[0]

    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] and tabuleiro[0][col] != ' ':
            return tabuleiro[0][col]

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
        return tabuleiro[0][2]

    return "Empate"

# Testando a função nos tabuleiros fornecidos
tabuleiros = [
    [
        ['X', 'O', 'X'],
        [' ', 'X', 'O'],
        ['O', ' ', 'X']
    ],
    [
        ['X', 'O', 'O'],
        ['X', 'X', 'O'],
        ['X', 'O', 'X']
    ],
    [
        [' ', ' ', ' '],
        ['X', ' ', 'O'],
        ['O', 'X', 'X']
    ],
    [
        ['O', 'O', 'O'],
        ['X', ' ', 'X'],
        ['O', 'X', 'X']
    ],
    [
        ['X', 'X', 'O'],
        ['X', ' ', 'O'],
        ['O', 'O', 'X']
    ]
]

for i, tabuleiro in enumerate(tabuleiros, start=1):
    print(f"Resultado do tabuleiro {i}: {avalia_tabuleiro(tabuleiro)}")
