# Entrada de dados
dividendo = int(input("Digite o valor do dividendo (número a ser dividido): "))
divisor = int(input("Digite o valor do divisor (número que divide): "))

# Processamento de dados
resultado = dividendo // divisor # divisão inteira
RESTO = dividendo % divisor # resto da divisão
# // para a divisão inteira (quantas vezes o divisor cabe dentro do dividendo)

# Saída de dados
print(f"{dividendo} / {divisor} = {resultado} | Resto = {RESTO}")

# Saída esperada:
# divisor / dividendo =
# resultado | resto = resto