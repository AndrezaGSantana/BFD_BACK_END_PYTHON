# Definindo a função que recebe um número variável de strings
def juntar_strings(*args):
    return "".join(args)  # junta todas as strings em uma só

resultado = juntar_strings("Olá", " ", "mundo", "!")
print(resultado)