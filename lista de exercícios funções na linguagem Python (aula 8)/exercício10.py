# Função lambda que verifica se um número é par
e_par = lambda x: x % 2 == 0

print("Verificador de Par ou Ímpar")
print("Digite números para verificar. Digite 'sair' para encerrar.\n")

while True:
    entrada = input("Número: ").strip()
    
    if entrada.lower() == 'sair':
        print("Encerrando o programa...")
        break

    # Verifica se a entrada é um número inteiro válido
    if entrada.lstrip('-').isdigit():  # permite números negativos
        numero = int(entrada)
        if e_par(numero):
            print(f"{numero} é par ✅\n")
        else:
            print(f"{numero} é ímpar ❌\n")
    else:
        print("Por favor, digite um número inteiro válido ou 'sair'.\n")