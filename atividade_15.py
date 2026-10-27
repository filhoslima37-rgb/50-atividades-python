# Atividade 15 - Sistema de votação
votos = {1: 0, 2: 0, 3: 0}
while True:
    try:
        voto = int(input("Vote em 1, 2 ou 3 (0 encerra): "))
    except ValueError:
        print("Entrada inválida.")
        continue
    if voto == 0:
        break
    if voto in votos:
        votos[voto] += 1
    else:
        print("Opção inválida.")
for opcao, total in votos.items():
    print(f"Opção {opcao}: {total} voto(s)")
