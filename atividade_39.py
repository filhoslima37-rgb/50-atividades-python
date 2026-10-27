# Atividade 39 - Maior valor e índice sem max()
numeros = [14, 7, 32, 5, 18, 41, 9, 27, 3, 36, 22, 11, 48, 16, 29, 2, 39, 20, 6, 33]
maior = numeros[0]
indice_maior = 0
for i in range(1, len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
        indice_maior = i
print(f"Maior valor: {maior}; índice: {indice_maior}")
