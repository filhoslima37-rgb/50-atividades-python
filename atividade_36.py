# Atividade 36 - Busca linear em dez números
numeros = [12, 5, 8, 21, 3, 17, 9, 30, 14, 6]
alvo = int(input("Número para buscar: "))
encontrado = False
for numero in numeros:
    if numero == alvo:
        encontrado = True
        break
print("Número encontrado." if encontrado else "Número não encontrado.")
