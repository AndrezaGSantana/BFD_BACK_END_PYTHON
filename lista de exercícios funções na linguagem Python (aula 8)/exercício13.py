# Lista de usuários
usuarios = [
    {'nome': 'Carlos', 'idade': 30},
    {'nome': 'Ana', 'idade': 25},
    {'nome': 'Bruno', 'idade': 40}
]

# Ordenando a lista pelo nome em ordem alfabética usando sorted e lambda
usuarios_ordenados = sorted(usuarios, key=lambda usuario: usuario['nome'])

# Resultado
print("Usuários ordenados por nome:")
for usuario in usuarios_ordenados:
    print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}")