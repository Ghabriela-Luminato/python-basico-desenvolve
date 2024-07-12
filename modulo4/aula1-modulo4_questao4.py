
n = int(input("Digite um número inteiro (n): "))


maior = 0

while n > 0:
    # Leia x
    x = int(input("Digite um número inteiro (x): "))
    
    if x > maior:
        maior = x
    
    n = n - 1

print(f"O maior número digitado foi: {maior}")
