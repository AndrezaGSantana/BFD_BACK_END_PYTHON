def calcular_media(*args):
    if len(args) == 0:
        return 0  # evita divisão por zero
    return sum(args) / len(args)

resultado = calcular_media(8.5, 9.0, 7.5)
print(f"Média: {resultado:.2f}")