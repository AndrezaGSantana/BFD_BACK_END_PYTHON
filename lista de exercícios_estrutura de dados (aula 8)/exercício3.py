# Entrada de dados:
vendas_semana = [1200, 1500, 1100, 2000, 2500, 1800, 1300]

# Total de vendas
total = sum(vendas_semana)

# Menor venda e o dia correspondente
menor_venda = min(vendas_semana)
dia_menor_venda = vendas_semana.index(menor_venda) + 1  # +1 para começar no dia 1

print("Total de vendas da semana:", total)
print(f"Menor venda: {menor_venda} no dia {dia_menor_venda}")