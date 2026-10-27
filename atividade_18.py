# Atividade 18 - Soma de dez valores
soma = 0
for i in range(1, 11):
    while True:
        try:
            n = int(input(f"Digite o {i}º inteiro: "))
            break
        except ValueError:
            print("Entrada inválida.")
    soma += n
print(f"Soma total: {soma}")
