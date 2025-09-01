# Entrada de dados
NOTA_MINIMA = 7.0
nota_final = float(input("Digite sua nota final: "))

# Condicional
if nota_final >= NOTA_MINIMA:
    print("Aprovado!")
elif nota_final >= 5.0:
    print("Você não foi muito bem. Mas ainda consegue recuperar")
else:
    print("Reprovado!")