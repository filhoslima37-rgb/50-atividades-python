# Atividade 47 - Insertion Sort mostrando cada inserção
numeros = [9, 4, 7, 2, 8, 1, 5]
print("Lista inicial:", numeros)
for i in range(1, len(numeros)):
    chave = numeros[i]
    j = i - 1
    while j >= 0 and numeros[j] > chave:
        numeros[j + 1] = numeros[j]
        j -= 1
    numeros[j + 1] = chave
    print(f"Após inserir {chave}: {numeros}")
print("Lista ordenada:", numeros)
