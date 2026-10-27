# Atividade 37 - Busca de nomes
nomes = []
for i in range(1, 11):
    nomes.append(input(f"Nome do aluno {i}: ").strip())
alvo = input("Nome para buscar: ").strip().casefold()
encontrado = False
for nome in nomes:
    if nome.casefold() == alvo:
        encontrado = True
        break
print("Aluno cadastrado." if encontrado else "Aluno não cadastrado.")
