# Atividade 34 - Média de dez notas válidas
soma = 0.0
quantidade = 0
for i in range(1, 11):
    while True:
        try:
            nota = float(input(f"Nota {i}/10: "))
            break
        except ValueError:
            print("Entrada inválida.")
    if nota < 0 or nota > 10:
        continue
    soma += nota
    quantidade += 1
if quantidade:
    print(f"Média das notas válidas: {soma / quantidade:.2f}")
else:
    print("Nenhuma nota válida foi informada.")
print(f"Notas válidas: {quantidade}")
