def buscar_livro(titulo, **kwargs):
    print(f"\nBuscando livro: {titulo}")
    
    if kwargs:
        print("Filtros aplicados:")
        for chave, valor in kwargs.items():
            print(f"{chave.capitalize()}: {valor}")
    else:
        print("Nenhum filtro aplicado.")

# Programa principal
titulo = input("Digite o título do livro: ").strip()

# Perguntar sobre filtros opcionais
filtros = {}
while True:
    opcao = input("Deseja adicionar um filtro de busca? (s/n): ").lower()
    if opcao == 'n':
        break
    chave = input("Nome do filtro (ex: autor, ano, genero): ").strip()
    valor = input(f"Valor para {chave}: ").strip()
    # tenta converter para inteiro se fizer sentido
    if valor.isdigit():
        valor = int(valor)
    filtros[chave] = valor

# Chamada da função
buscar_livro(titulo, **filtros)