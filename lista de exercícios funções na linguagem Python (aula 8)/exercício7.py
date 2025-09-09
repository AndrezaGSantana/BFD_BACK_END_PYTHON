def cadastrar_usuario(nome, email, **kwargs):
    print("\nFicha de Cadastro:")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    
    # Mostra os demais dados opcionais
    for chave, valor in kwargs.items():
        print(f"{chave.capitalize()}: {valor}")

# Programa principal - pedindo dados ao usuário
nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")

# Perguntando se o usuário quer adicionar outros dados
outros_dados = {}
while True:
    opcao = input("Deseja adicionar outro dado? (s/n): ").lower()
    if opcao == 'n':
        break
    chave = input("Nome do dado (ex: idade, cidade, profissão): ")
    valor = input(f"Valor para {chave}: ")
    outros_dados[chave] = valor

# Chamada da função
cadastrar_usuario(nome, email, **outros_dados)