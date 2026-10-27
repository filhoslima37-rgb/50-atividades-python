# Atividade 35 - Filtrar nomes que não começam com A
nomes = [
    "Ana", "Bruno", "Carlos", "Amanda", "Daniel",
    "Alice", "Fernanda", "André", "Gabriel", "Beatriz"
]
for nome in nomes:
    if nome.strip().lower().startswith("a"):
        continue
    print(nome)
