# Atividade 46 - Selection Sort
numeros = [29, 10, 14, 37, 13, 5, 22, 8, 31, 17]
for i in range(len(numeros) - 1):
    indice_menor = i
    for j in range(i + 1, len(numeros)):
        if numeros[j] < numeros[indice_menor]:
            indice_menor = j
    numeros[i], numeros[indice_menor] = numeros[indice_menor], numeros[i]
print("Ordem crescente:", numeros)
