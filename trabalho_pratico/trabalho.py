# Dados iniciais
usuarios = {
    'gerente': ['Gerente', 'senha123', 'gerente', ['C', 'R', 'U', 'D']],
    'funcionario': ['Funcionário', 'senha456', 'funcionario', ['C', 'R']],
    'cliente': ['Cliente', 'senha789', 'cliente', []]
}

produtos = [
    {'nome': 'Notebook', 'preco': 3500.00, 'quantidade': 10},
    {'nome': 'Smartphone', 'preco': 2500.00, 'quantidade': 20},
    {'nome': 'Tablet', 'preco': 1200.00, 'quantidade': 15},
    {'nome': 'Assistência Técnica', 'preco': 200.00, 'quantidade': 50}
]

# Funções para CRUD de usuários
def criar_usuario(nome, senha, tipo, permissoes=[]):
    usuarios[nome] = [nome, senha, tipo, permissoes]

def listar_usuarios():
    for usuario in usuarios.values():
        print(f"Nome: {usuario[0]}, Tipo: {usuario[2]}, Permissões: {usuario[3]}")

def atualizar_usuario(nome, senha, tipo, permissoes=[]):
    if nome in usuarios:
        usuarios[nome] = [nome, senha, tipo, permissoes]
    else:
        print(f"Usuário {nome} não encontrado.")

def deletar_usuario(nome):
    if nome in usuarios:
        del usuarios[nome]
    else:
        print(f"Usuário {nome} não encontrado.")

# Funções específicas de usuários
def listar_usuarios_por_tipo(tipo):
    for usuario in usuarios.values():
        if usuario[2] == tipo:
            print(f"Nome: {usuario[0]}, Tipo: {usuario[2]}, Permissões: {usuario[3]}")

def validar_login(nome, senha):
    if nome in usuarios and usuarios[nome][1] == senha:
        return True
    return False

# Funções para CRUD de produtos/serviços
def criar_produto(nome, preco, quantidade):
    produtos.append({'nome': nome, 'preco': preco, 'quantidade': quantidade})

def listar_produtos():
    for produto in produtos:
        print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

def buscar_produto_por_nome(nome):
    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            return produto
    return None

def ordenar_produtos_por_nome():
    produtos_ordenados = sorted(produtos, key=lambda x: x['nome'])
    for produto in produtos_ordenados:
        print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

def ordenar_produtos_por_preco():
    produtos_ordenados = sorted(produtos, key=lambda x: x['preco'])
    for produto in produtos_ordenados:
        print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

# Exemplo de uso das funções (simulado)
if __name__ == "__main__":
    # Exemplo de operações de usuários
    print("Lista de Usuários:")
    listar_usuarios()
    print()

    print("Criando novo usuário...")
    criar_usuario('novo_funcionario', 'senha123', 'funcionario', ['C', 'R'])
    print("Lista de Usuários atualizada:")
    listar_usuarios()
    print()

    print("Atualizando usuário existente...")
    atualizar_usuario('funcionario', 'novasenha456', 'funcionario', ['C', 'R', 'U'])
    print("Lista de Usuários atualizada:")
    listar_usuarios()
    print()

    print("Deletando usuário...")
    deletar_usuario('novo_funcionario')
    print("Lista de Usuários atualizada:")
    listar_usuarios()
    print()

    # Exemplo de operações de produtos
    print("Lista de Produtos:")
    listar_produtos()
    print()

    print("Buscando produto por nome:")
    produto = buscar_produto_por_nome('Tablet')
    if produto:
        print(f"Produto encontrado: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
    else:
        print("Produto não encontrado.")
    print()

    print("Ordenando produtos por nome:")
    ordenar_produtos_por_nome()
    print()

    print("Ordenando produtos por preço:")
    ordenar_produtos_por_preco()
    print()
