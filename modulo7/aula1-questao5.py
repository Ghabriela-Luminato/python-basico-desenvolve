

def pares_unicos(numeros, soma_objetivo):
    pares = []
    vistos = set()
    for num in numeros:
        complemento = soma_objetivo - num
        if complemento in vistos:
            pares.append((complemento, num))
        vistos.add(num)
    return pares

nums = [3, 4, 5, 6, 7]
soma = 10
resultado = pares_unicos(nums, soma)
print(resultado)  
