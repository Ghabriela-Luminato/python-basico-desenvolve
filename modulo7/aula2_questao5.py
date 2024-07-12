

import random

def embaralhar_palavras(frase):
    def embaralhar(palavra):
        if len(palavra) > 3:
            miolo = list(palavra[1:-1])
            random.shuffle(miolo)
            return palavra[0] + ''.join(miolo) + palavra[-1]
        return palavra

    palavras = frase.split()
    palavras_embaralhadas = [embaralhar(palavra) for palavra in palavras]
    return ' '.join(palavras_embaralhadas)


frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)

