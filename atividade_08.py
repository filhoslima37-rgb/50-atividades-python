# Atividade 08 - Validação de idade
while True:
    try:
        idade = int(input("Digite sua idade (0 a 120): "))
        if 0 <= idade <= 120:
            print(f"Idade válida: {idade}")
            break
        print("Idade inválida. Tente novamente.")
    except ValueError:
        print("Digite um número inteiro.")
