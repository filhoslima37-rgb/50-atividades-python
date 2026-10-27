# Atividade 29 - Adivinhar número secreto
# Número fixo para tornar o exercício reproduzível; altere se desejar.
secreto = 13
while True:
    try:
        palpite = int(input("Adivinhe o número secreto (1 a 20): "))
    except ValueError:
        print("Digite um inteiro.")
        continue
    if not 1 <= palpite <= 20:
        print("Digite um número entre 1 e 20.")
    elif palpite < secreto:
        print("O número secreto é maior.")
    elif palpite > secreto:
        print("O número secreto é menor.")
    else:
        print("Acertou!")
        break
