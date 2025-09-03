# Entrada de dados
venda = ('Caderno', 15)
preco_unitario = 25.00

produto, quantidade = venda
total = quantidade * preco_unitario

print(f"Produto: {produto}", f"\nQuantidade: {quantidade}", 
      f"\nValor total da venda: R$", total)