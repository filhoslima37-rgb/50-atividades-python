# Atividade 49 - Sistema de controle de estoque
produtos = []

def cadastrar_produto():
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Nome inválido.")
        return
    try:
        quantidade = int(input("Quantidade inicial: "))
        if quantidade < 0:
            print("A quantidade não pode ser negativa.")
            return
    except ValueError:
        print("Quantidade inválida.")
        return
    for produto in produtos:
        if produto["nome"].casefold() == nome.casefold():
            produto["quantidade"] += quantidade
            print("Produto existente: quantidade atualizada.")
            return
    produtos.append({"nome": nome, "quantidade": quantidade})
    print("Produto cadastrado.")

def buscar_produto():
    alvo = input("Nome para buscar: ").strip().casefold()
    for produto in produtos:
        if produto["nome"].casefold() == alvo:
            print(f"{produto['nome']}: {produto['quantidade']} unidade(s)")
            return
    print("Produto não encontrado.")

while True:
    print("\n1 - Cadastrar/adicionar produto\n2 - Buscar produto\n3 - Listar em ordem alfabética\n0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "0":
        break
    elif opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        buscar_produto()
    elif opcao == "3":
        for produto in sorted(produtos, key=lambda item: item["nome"].casefold()):
            print(f"{produto['nome']}: {produto['quantidade']}")
    else:
        print("Opção inválida.")
