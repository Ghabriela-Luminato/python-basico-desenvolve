
idade = int(input("Digite sua idade: "))
jogou_tres_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ").lower() == 'true'
venceu_jogo = int(input("Quantas vezes venceu um jogo? "))


apto_ingresso = idade >= 16 and idade <= 18 and jogou_tres_jogos and venceu_jogo >= 1


print("Apto para ingressar no clube de jogos de tabuleiro:", apto_ingresso)
