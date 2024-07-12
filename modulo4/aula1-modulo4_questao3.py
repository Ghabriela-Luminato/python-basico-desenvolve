
n1 = float(input("Digite a primeira nota (n1): "))
n2 = float(input("Digite a segunda nota (n2): "))
n3 = float(input("Digite a terceira nota (n3): "))

m = (n1 + n2 + n3) / 3


if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

print("Fim")
