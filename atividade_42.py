# Atividade 42 - Comparação entre busca linear e binária
def busca_linear(lista, alvo):
    comparacoes = 0
    for i, valor in enumerate(lista):
        comparacoes += 1
        if valor == alvo:
            return i, comparacoes
    return -1, comparacoes

def busca_binaria(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    comparacoes = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if lista[meio] == alvo:
            return meio, comparacoes
        if lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes

numeros = list(range(2, 41, 2))
alvo = int(input("Número par para buscar: "))
indice_l, comp_l = busca_linear(numeros, alvo)
indice_b, comp_b = busca_binaria(numeros, alvo)
print(f"Linear: índice={indice_l}, comparações={comp_l}")
print(f"Binária: índice={indice_b}, comparações={comp_b}")
