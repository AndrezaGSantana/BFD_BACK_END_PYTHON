# Listas de nomes e sobrenomes
nomes = ['João', 'Maria', 'Pedro']
sobrenomes = ['Silva', 'Santos', 'Rocha']

# Combinando nomes e sobrenomes usando map e lambda
nomes_completos = list(map(lambda n, s: f"{n} {s}", nomes, sobrenomes))

# Resultado
print("Nomes completos:", nomes_completos)