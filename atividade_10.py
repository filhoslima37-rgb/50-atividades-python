# Atividade 10 - Maior número até zero
maior = None
while True:
    try:
        n = int(input("Digite um inteiro (0 encerra): "))
    except ValueError:
        print("Entrada inválida.")
        continue
    if n == 0:
        break
    if maior is None or n > maior:
        maior = n
if maior is None:
    print("Nenhum número foi informado antes do zero.")
else:
    print(f"Maior número: {maior}")
