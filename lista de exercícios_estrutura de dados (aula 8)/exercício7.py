catalogo = {
    'nome': 'Mouse Gamer',
    'preço': 150.00,
    'estoque': 50
}

novo_produto = {
    'nome': 'Teclado Mecânico',
    'preço': 450.00,
    'estoque': 30
}

catalogo.update(novo_produto)

print("Catálogo atualizado:")
for chave, valor in catalogo.items():
    print(chave, ":", valor)