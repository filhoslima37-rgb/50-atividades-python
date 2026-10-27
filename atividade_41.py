# Atividade 41 - Busca binária
numeros = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59]
alvo = int(input("Número para buscar: "))
inicio, fim = 0, len(numeros) - 1
indice = -1
while inicio <= fim:
    meio = (inicio + fim) // 2
    if numeros[meio] == alvo:
        indice = meio
        break
    if numeros[meio] < alvo:
        inicio = meio + 1
    else:
        fim = meio - 1
print(f"Encontrado no índice {indice}." if indice >= 0 else "Número não encontrado.")
