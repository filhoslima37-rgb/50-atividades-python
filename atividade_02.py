# Atividade 02 - Contagem regressiva
while True:
    try:
        n = int(input("Digite um inteiro positivo: "))
        if n >= 0:
            break
        print("Digite um valor maior ou igual a zero.")
    except ValueError:
        print("Entrada inválida.")
while n >= 0:
    print(n)
    n -= 1
