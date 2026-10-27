# Atividade 45 - Bubble Sort
numeros = []
for i in range(1, 11):
    numeros.append(int(input(f"Digite o inteiro {i}/10: ")))
for fim in range(len(numeros) - 1, 0, -1):
    houve_troca = False
    for i in range(fim):
        if numeros[i] > numeros[i + 1]:
            numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
            houve_troca = True
    if not houve_troca:
        break
print("Ordem crescente:", numeros)
