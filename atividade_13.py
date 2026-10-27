# Atividade 13 - Solicitar número positivo
while True:
    try:
        n = int(input("Digite um inteiro positivo: "))
        if n > 0:
            print(f"Valor aceito: {n}")
            break
        print("O valor precisa ser maior que zero.")
    except ValueError:
        print("Entrada inválida.")
