# Entrada de dados
estoque = ['camiseta', 'calça', 'meia', 'jaqueta']
print("Estoque inicial:", estoque)

# Adicionando o novo produto ''boné''
estoque.append('boné')
print("Após adicionar 'boné':", estoque)

# Removendo o produto ''calça'' que não tem estoque disponível
estoque.remove('calça')
print("Após remover 'calça':", estoque)