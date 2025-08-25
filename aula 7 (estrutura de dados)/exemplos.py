# Lista vazia
minha_lista = []

# Lista com elementos
numeros = [10, 20, 30, 40]
nomes = ["Alice", "Bob", "Carlos"]
mista = [1,"Python", True, 3.14]

# Índice________________________________________________________ 

# Listas
frutas = ["Maçã", "Banana", "Cereja"]

# Acessa o primeiro elemento (índice 0)
print(frutas[0]) # Saída: Maçã

# Acessa o primeiro elemento (índice 1)
print(frutas[1]) # Saída: Banana

# Acessa o primeiro elemento (índice 2)
print(frutas[2]) # Saída: Cereja


# Append___________________________________________________________

print(frutas)
frutas.append("Uva") # Resultado: [Maçã, Banana, Cereja, Uva]
print(frutas) 

# Insert___________________________________________________________

print(frutas)
frutas.insert(1,"Kiwi") # Resultado: [Maçã, Kiwi, Banana, Cereja, Uva]
print(frutas)

# Remove____________________________________________________________

print(frutas)
frutas.remove("Kiwi") # Resultado: [Maçã, Banana, Cereja, Uva]
print(frutas) 

# Pop________________________________________________________________

print(frutas)
frutas.pop(0) # Resultado: [Banana, Cereja, Uva]
print(frutas)

# Sort_______________________________________________________________

pontos = [85, 92, 78, 60]
pontos.sort() # Saída esperada: [60, 78, 85, 92]
print(pontos)

# Reverse____________________________________________________________

pontos.reverse()
print(pontos)

# Sort (Ordem decrescente)____________________________________________

pontos.sort(reverse=True)
print(pontos)

# Count_______________________________________________________________

vogais = ["a", "e", "a", "o"]
contagem = vogais.count("a")
print(contagem)

# Index____________________________________________________________________

indice = vogais.index("e")
print(indice)

# Len_______________________________________________________________________

cidades = ["Lisboa", "Porto"]
tamanho = len(cidades)
print(tamanho)

# Del___________________________________________________________________________

print(frutas)
del frutas[0]
print(frutas)

# Clear______________________________________________________________________________

print(frutas)
frutas.clear()
print(frutas)