# Atividade 07 - Tabuada com while
try:
    numero = int(input("Digite um inteiro: "))
    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1
except ValueError:
    print("Entrada inválida.")
