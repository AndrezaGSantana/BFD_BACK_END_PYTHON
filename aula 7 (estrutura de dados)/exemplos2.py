# Lista
frutas = ["Maçã", "Banana", "Cereja", "Morango", "Uva"]
precos = [8.20, 3.56, 16.34, 10.50, 10.00]

frutas_fatiados = frutas[0:3]
precos_fatiados = precos[0:3]

precos_fatiados = [precos * 2 for precos in precos_fatiados]
print(precos_fatiados)