def contar_vogais(texto):
    vogais = "aeiouAEIOU"  # considerando maiúsculas e minúsculas
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

entrada = input("Digite um texto: ")
resultado = contar_vogais(entrada)

print("Quantidade de vogais:", resultado)