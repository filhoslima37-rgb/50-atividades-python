# Atividade 27 - Controle de estoque
while True:
    try:
        estoque = int(input("Quantidade inicial do estoque: "))
        if estoque >= 0:
            break
        print("O estoque não pode ser negativo.")
    except ValueError:
        print("Digite um inteiro.")
while estoque > 0:
    print(f"Estoque atual: {estoque}")
    try:
        retirada = int(input("Quantidade a retirar: "))
    except ValueError:
        print("Entrada inválida.")
        continue
    if retirada <= 0:
        print("A retirada deve ser positiva.")
    elif retirada > estoque:
        print("Retirada maior que o estoque disponível.")
    else:
        estoque -= retirada
print("Estoque zerado.")
