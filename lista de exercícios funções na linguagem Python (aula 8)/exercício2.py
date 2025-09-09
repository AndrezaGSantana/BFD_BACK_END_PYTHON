# Função que recebe um texto como argumento
def inverter_texto(texto):
    return texto[::-1]   # fatia a string ao contrário

entrada = input("Digite um texto: ")
resultado = inverter_texto(entrada)

print("Texto invertido:", resultado)