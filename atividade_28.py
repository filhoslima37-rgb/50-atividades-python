# Atividade 28 - Simulação bancária
saldo = 0.0
while True:
    print(f"\nSaldo atual: R$ {saldo:.2f}\n1 - Depositar\n2 - Sacar\n0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "0":
        break
    if opcao not in ("1", "2"):
        print("Opção inválida.")
        continue
    try:
        valor = float(input("Valor: R$ "))
    except ValueError:
        print("Valor inválido.")
        continue
    if valor <= 0:
        print("O valor deve ser positivo.")
    elif opcao == "1":
        saldo += valor
        print("Depósito realizado.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        print("Saque realizado.")
print(f"Saldo final: R$ {saldo:.2f}")
