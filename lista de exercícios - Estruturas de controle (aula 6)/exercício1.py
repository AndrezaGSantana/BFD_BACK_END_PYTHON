# Entrada de dados
IDADE_MINIMA = 18
idade_usuario = int(input("Digite sua idade: "))

# Condicional
if idade_usuario >= IDADE_MINIMA:
    print("O usuário é maior de idade.")
elif idade_usuario >= 16:
    print("O usuário é menor e tem 16 ou 17 anos.")
else:
    print("O usuário é menor de 16 anos.")