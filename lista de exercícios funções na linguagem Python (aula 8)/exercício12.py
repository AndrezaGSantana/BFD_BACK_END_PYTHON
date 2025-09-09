# Lista de preços
precos = [85, 120, 50, 250, 99]

# Filtro de preços maiores que 100 usando filter e lambda
produtos_filtrados = list(filter(lambda x: x > 100, precos))

# Resultado
print("Preços filtrados (maiores que 100):", produtos_filtrados)