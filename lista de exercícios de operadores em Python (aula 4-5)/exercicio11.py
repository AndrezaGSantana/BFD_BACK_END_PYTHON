# Esntrada de dados
IDADE_MINIMA = 18
idade_usuario = int(input("Informe a sua idade: "))

# Verificando se o usuário é maior de idade
maior_de_idade = idade_usuario >= IDADE_MINIMA

# Verificando se o usuário é menor de 18
menor_de_idade = idade_usuario < IDADE_MINIMA

# Exibindo os resultados
print(f"O usuário é maior de idade? {maior_de_idade}")
print(f"O usuário é menor de idade? {menor_de_idade}")

# Saída esperada: "O usuário é maior de idade? operação_de_comparação" e "O usuário é menor de idade?

