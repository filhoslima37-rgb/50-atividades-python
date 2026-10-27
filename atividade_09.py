# Atividade 09 - Fatorial com while
while True:
    try:
        n = int(input("Digite um inteiro não negativo: "))
        if n >= 0:
            break
        print("O número deve ser não negativo.")
    except ValueError:
        print("Entrada inválida.")
fatorial = 1
contador = 1
while contador <= n:
    fatorial *= contador
    contador += 1
print(f"{n}! = {fatorial}")
