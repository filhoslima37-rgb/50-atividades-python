# Atividade 14 - Cadastro de alunos
nomes = []
while True:
    nome = input("Nome do aluno: ").strip()
    if nome:
        nomes.append(nome)
    else:
        print("Nome vazio não cadastrado.")
    continuar = input("Deseja cadastrar outro? (s/n): ").strip().lower()
    if continuar != "s":
        break
print("\nAlunos cadastrados:")
for i, nome in enumerate(nomes, start=1):
    print(f"{i}. {nome}")
