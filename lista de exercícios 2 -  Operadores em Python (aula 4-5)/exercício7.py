# Entrada de dados
idade_motorista = int(input("Qual a sua idade? "))
tem_carteira = bool(input("Você tem carteira de motorista? (True/False) "))  == True # Código originalmente digitado sem o ""== True" no final

# Condicional
pode_dirigir = idade_motorista > 18 and tem_carteira == True 
# Código original, estava idade_motorista > 18 or tem_carteira == True, o que permitiria alguém com 16 anos e carteira (ou até só carteira sem idade mínima)

# Saída de dados
print(f"Pode dirigir? {pode_dirigir}")

#Saída esperada: Pode dirigir? True