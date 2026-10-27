# Atividade 19 - Média de cinco notas
notas = []
for i in range(1, 6):
    while True:
        try:
            nota = float(input(f"Digite a nota {i} (0 a 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida.")
media = sum(notas) / len(notas)
print(f"Média: {media:.2f}")
print("Aprovado." if media >= 7 else "Reprovado.")
