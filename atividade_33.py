# Atividade 33 - Ignorar múltiplos de três
for n in range(1, 101):
    if n % 3 == 0:
        continue
    print(n)
