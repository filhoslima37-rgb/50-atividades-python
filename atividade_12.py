# Atividade 12 - Menu de operações
while True:
    print("\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "0":
        print("Programa encerrado.")
        break
    if opcao not in ("1", "2", "3"):
        print("Opção inválida.")
        continue
    try:
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))
    except ValueError:
        print("Digite números válidos.")
        continue
    if opcao == "1":
        resultado = a + b
    elif opcao == "2":
        resultado = a - b
    else:
        resultado = a * b
    print(f"Resultado: {resultado:g}")
