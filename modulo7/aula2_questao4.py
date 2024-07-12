

import re

def validador_senha(senha):
    if (len(senha) >= 8 and
        re.search(r'[A-Z]', senha) and
        re.search(r'[a-z]', senha) and
        re.search(r'\d', senha) and
        re.search(r'[@#$]', senha)):
        return True
    return False

# Exemplo de uso:
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))  
print(validador_senha(senha2))  
print(validador_senha(senha3))  
