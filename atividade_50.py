# Atividade 50 - Sistema de análise de números
numeros = []

def cadastrar_numeros():
    numeros.clear()
    for i in range(1, 21):
        while True:
            try:
                numeros.append(int(input(f"Número {i}/20: ")))
                break
            except ValueError:
                print("Digite um inteiro.")

def busca_linear(lista, alvo):
    comparacoes = 0
    for i, valor in enumerate(lista):
        comparacoes += 1
        if valor == alvo:
            return i, comparacoes
    return -1, comparacoes

def busca_binaria(lista, alvo):
    ordenada = sorted(lista)
    inicio, fim = 0, len(ordenada) - 1
    comparacoes = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if ordenada[meio] == alvo:
            return meio, comparacoes
        if ordenada[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes

while True:
    print("\n1 - Cadastrar 20 números\n2 - Média\n3 - Maior e menor\n4 - Ordem crescente\n5 - Ordem decrescente\n6 - Busca linear\n7 - Busca binária\n0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "0":
        break
    if opcao == "1":
        cadastrar_numeros()
    elif not numeros:
        print("Cadastre os 20 números primeiro.")
    elif opcao == "2":
        print(f"Média: {sum(numeros) / len(numeros):.2f}")
    elif opcao == "3":
        maior, menor = numeros[0], numeros[0]
        for n in numeros[1:]:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        print(f"Maior: {maior}; menor: {menor}")
    elif opcao == "4":
        print("Crescente:", sorted(numeros))
    elif opcao == "5":
        print("Decrescente:", sorted(numeros, reverse=True))
    elif opcao in ("6", "7"):
        try:
            alvo = int(input("Número a pesquisar: "))
        except ValueError:
            print("Entrada inválida.")
            continue
        if opcao == "6":
            indice, comparacoes = busca_linear(numeros, alvo)
            print(f"Busca linear: índice={indice}, comparações={comparacoes}")
        else:
            indice, comparacoes = busca_binaria(numeros, alvo)
            print(f"Busca binária (lista ordenada): índice={indice}, comparações={comparacoes}")
    else:
        print("Opção inválida.")
print("Sistema encerrado.")
