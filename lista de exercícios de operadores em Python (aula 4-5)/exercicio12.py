# Variáveis
tem_wifi = False
tem_dados_moveis = True

# Verificação se pode se conectar à internet
pode_conectar = tem_wifi or tem_dados_moveis

# Exibição do resultado
print(f"O celular pode se conectar à internet? {pode_conectar}")

# Saída esperada: “O celular pode se conectar a internet? [ resultado da operação lógica ]