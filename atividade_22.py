# Atividade 22 - Contagem de vogais
palavra = input("Digite uma palavra: ")
vogais = "aeiouáéíóúâêîôûãõà"
quantidade = 0
for letra in palavra.lower():
    if letra in vogais:
        quantidade += 1
print(f"Quantidade de vogais: {quantidade}")
