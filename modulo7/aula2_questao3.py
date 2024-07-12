

def eh_palindromo(frase):
    frase = ''.join(filter(str.isalnum, frase)).lower()
    return frase == frase[::-1]

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == 'fim':
        break
    if eh_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
