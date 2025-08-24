saldo_bancario = 1000
print("Saldo inicial:", saldo_bancario)

# Solicita ao usuário os valores
deposito = float(input("Informe o valor do depósito: "))
saque = float(input("Informe o valor do saque: "))
fator_juros = float(input("Informe o fator de juros: "))

# Adiciona o depósito ao saldo
saldo_bancario += deposito
print("Após depósito:", saldo_bancario)

# Subtrai o saque do saldo
saldo_bancario -= saque
print("Após saque:", saldo_bancario)

# Aplica o fator de juros ao saldo
saldo_bancario *= fator_juros
print("Após aplicação de juros:", saldo_bancario)

# Mostra o saldo final
print("Saldo final:", saldo_bancario)