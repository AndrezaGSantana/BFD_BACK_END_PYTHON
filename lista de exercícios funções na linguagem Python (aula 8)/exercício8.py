def atualizar_perfil(perfil, **kwargs):
    perfil.update(kwargs)  # atualiza ou adiciona novas chaves
    return perfil

# Programa principal
perfil = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}

print("Perfil atual:")
for chave, valor in perfil.items():
    print(f"{chave.capitalize()}: {valor}")

print("\nAtualizar informações do perfil:")
novos_dados = {}
while True:
    opcao = input("Deseja atualizar algum dado? (s/n): ").lower()
    if opcao == 'n':
        break
    chave = input("Qual informação deseja atualizar (ex: nome, idade, cidade)? ").lower()
    valor = input(f"Novo valor para {chave}: ")
    # tenta converter para inteiro se fizer sentido
    if valor.isdigit():
        valor = int(valor)
    novos_dados[chave] = valor

# Atualizando o perfil
perfil_atualizado = atualizar_perfil(perfil, **novos_dados)

print("\nPerfil atualizado:")
for chave, valor in perfil_atualizado.items():
    print(f"{chave.capitalize()}: {valor}")