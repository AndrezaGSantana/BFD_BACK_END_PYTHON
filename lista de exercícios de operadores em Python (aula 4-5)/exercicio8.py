# Entrada de dados:
saldo_bancario = 1000
deposito = float(input("Informe o valor do depósito: "))
saque = float(input("Informe o valor do saque: "))
fator_juros = float(input("Informe o fator de juros: "))

# Adiciona o depósito ao saldo
saldo_bancario += deposito

# Subtrai o saque do saldo
saldo_bancario -= saque

# Aplica o fator de juros ao saldo
saldo_bancario *= fator_juros

# Mostra o saldo final
print("Saldo final:", saldo_bancario)