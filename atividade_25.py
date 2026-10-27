# Atividade 25 - Análise das notas de dez alunos
notas = []
for i in range(1, 11):
    while True:
        try:
            nota = float(input(f"Nota do aluno {i} (0 a 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida.")
print(f"Maior nota: {max(notas):.2f}")
print(f"Menor nota: {min(notas):.2f}")
print(f"Média da turma: {sum(notas) / len(notas):.2f}")
