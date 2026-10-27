# Atividade 40 - Menor valor e índice sem min()
numeros = [14, 7, 32, 5, 18, 41, 9, 27, 3, 36, 22, 11, 48, 16, 29, 2, 39, 20, 6, 33]
menor = numeros[0]
indice_menor = 0
for i in range(1, len(numeros)):
    if numeros[i] < menor:
        menor = numeros[i]
        indice_menor = i
print(f"Menor valor: {menor}; índice: {indice_menor}")
