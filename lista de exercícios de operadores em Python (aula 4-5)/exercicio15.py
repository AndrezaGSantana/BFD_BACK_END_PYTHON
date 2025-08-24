# Variável
senha = "Python123"

# Verificação combinando todas as condições com and e not
senha_valida = (not senha == "") and (senha == "Python123") and (not senha == "123456")

# Exibição do resultado
print(f"A senha é válida? {senha_valida}")

# Saída esperada: A senha é válida? senha_valida