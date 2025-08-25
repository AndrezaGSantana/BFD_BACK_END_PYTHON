# Sem usar as listas de compreensão
numeros = [1, 2, 3, 4, 5]
pares = []
for num in numeros:
    if num % 2 ==0:
        pares.append(num)
print(pares)

# Usando as listas de compreensão
numeros = [1, 2, 3, 4, 5]
pares = [num for num in numeros if num %2 == 0]
print(pares)