# Atividade 38 - Busca com índice
numeros = [10, 25, 7, 42, 18, 3, 31]
try:
    alvo = int(input("Valor para buscar: "))
except ValueError:
    print("Entrada inválida.")
else:
    indice = -1
    for i in range(len(numeros)):
        if numeros[i] == alvo:
            indice = i
            break
    if indice >= 0:
        print(f"Valor encontrado no índice {indice}.")
    else:
        print("Valor não encontrado.")
