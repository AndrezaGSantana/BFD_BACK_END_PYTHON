# Lista de vendedores
vendedores = ['João', 'Maria', 'Pedro', 'Ana']

# Percorrendo a lista, começando a contagem do 1
for posicao, nome in enumerate(vendedores, start=1):
    print(f"{posicao}º - {nome}")