# Atividade 43 - Ordenação crescente com sorted()
numeros = []
for i in range(1, 11):
    numeros.append(int(input(f"Digite o inteiro {i}/10: ")))
print("Ordem crescente:", sorted(numeros))
