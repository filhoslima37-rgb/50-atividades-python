# Atividade 24 - Primeiros 15 termos de Fibonacci
a, b = 0, 1
for _ in range(15):
    print(a)
    a, b = b, a + b
