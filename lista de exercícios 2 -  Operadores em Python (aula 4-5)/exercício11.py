# Entrada de dados
km_percorridos = float(input("Digite a quantidade de km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias de aluguel: "))

# Cálculo 
preco = (dias_alugados * 60) + (km_percorridos * 0.15)

# Saída de dados
print(f"O preço a pagar é: R$ {preco:.2f}") # Formatação do valor com duas casas decimais "arredondando" o valor
