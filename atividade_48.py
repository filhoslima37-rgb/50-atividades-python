# Atividade 48 - Sistema de gerenciamento de alunos
alunos = []

def cadastrar():
    nome = input("Nome do aluno: ").strip()
    if not nome:
        print("Nome não pode ficar vazio.")
        return
    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Nota {i} (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                print("Nota deve estar entre 0 e 10.")
            except ValueError:
                print("Entrada inválida.")
    alunos.append({"nome": nome, "notas": notas})
    print("Aluno cadastrado.")

def pesquisar():
    alvo = input("Nome para pesquisar: ").strip().casefold()
    for aluno in alunos:
        if aluno["nome"].casefold() == alvo:
            media = sum(aluno["notas"]) / len(aluno["notas"])
            print(f"Nome: {aluno['nome']} | Notas: {aluno['notas']} | Média: {media:.2f}")
            return
    print("Aluno não encontrado.")

while True:
    print("\n1 - Cadastrar aluno\n2 - Listar alunos\n3 - Pesquisar aluno\n0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "0":
        break
    elif opcao == "1":
        cadastrar()
    elif opcao == "2":
        for aluno in alunos:
            media = sum(aluno["notas"]) / len(aluno["notas"])
            print(f"{aluno['nome']} - média {media:.2f}")
        if not alunos:
            print("Nenhum aluno cadastrado.")
    elif opcao == "3":
        pesquisar()
    else:
        print("Opção inválida.")
print("Sistema encerrado.")
