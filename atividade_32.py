# Atividade 32 - Somar dez valores não negativos
soma = 0
for i in range(1, 11):
    while True:
        try:
            n = int(input(f"Digite o inteiro {i}/10: "))
            break
        except ValueError:
            print("Entrada inválida.")
    if n < 0:
        continue
    soma += n
print(f"Soma dos valores não negativos: {soma}")
