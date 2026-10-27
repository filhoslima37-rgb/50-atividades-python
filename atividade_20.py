# Atividade 20 - Potenciação com multiplicações sucessivas
try:
    base = float(input("Base: "))
    expoente = int(input("Expoente inteiro não negativo: "))
    if expoente < 0:
        print("O expoente deve ser não negativo.")
    else:
        resultado = 1
        for _ in range(expoente):
            resultado *= base
        print(f"Resultado: {resultado:g}")
except ValueError:
    print("Entrada inválida.")
