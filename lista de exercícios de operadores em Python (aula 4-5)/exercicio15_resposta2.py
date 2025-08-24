# Variável
senha = "Python123"

# Verificação das condições
senha_valida = (
    senha != "" and         # não está vazia
    senha == "Python123" and # exatamente igual à senha correta
    senha != "123456"       # diferente de senha comum
)

print(f"A senha é válida? {senha_valida}")

# Saída esperada: A senha é válida? senha_valida
