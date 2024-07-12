
n = int(input("Digite n: "))
matriz = [[i * j for j in range(n)] for i in range(n)]
print("Matriz:")
for linha in matriz:
    print(linha)
