# Funções
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

try:
    # Entrada dos números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Entrada
    op = input("Digite a operação desejada (+, -, *, /): ")

    # Verificação
    if op == "+":
        resultado = soma(num1, num2)
    elif op == "-":
        resultado = subtracao(num1, num2)
    elif op == "*":
        resultado = multiplicacao(num1, num2)
    elif op == "/":
        if num2 == 0:
            raise ZeroDivisionError("Erro: divisão por zero")
        resultado = divisao(num1, num2)
    else:
        raise ValueError("Erro: operação inválida")

except ValueError as ve:
    print(ve)

except ZeroDivisionError as zde:
    print(zde)

except Exception:
    print("Erro: valor inválido")

else:
    print("Resultado:", resultado)

finally:
    print("Fim do programa")