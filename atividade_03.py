# Atividade 03 - Soma de números até zero
soma = 0
while True:
    try:
        n = int(input("Digite um inteiro (0 encerra): "))
    except ValueError:
        print("Entrada inválida.")
        continue
    if n == 0:
        break
    soma += n
print(f"Soma: {soma}")
