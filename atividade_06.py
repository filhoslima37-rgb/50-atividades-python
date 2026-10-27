# Atividade 06 - Média de notas até -1
soma = 0.0
quantidade = 0
while True:
    try:
        nota = float(input("Digite uma nota (-1 encerra): "))
    except ValueError:
        print("Entrada inválida.")
        continue
    if nota == -1:
        break
    if 0 <= nota <= 10:
        soma += nota
        quantidade += 1
    else:
        print("Nota fora do intervalo de 0 a 10; ignorada.")
if quantidade:
    print(f"Média: {soma / quantidade:.2f}")
else:
    print("Nenhuma nota válida informada.")
