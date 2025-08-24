# Entrada de dados:
tarefas = 20
numero_pessoas = int(input("Quantidade de pessoas para a execução da tarefa: "))

# Divide as tarefas igualmente entre as pessoas, usando divisão inteira
tarefas //= numero_pessoas
print(f"Cada pessoa recebeu:", tarefas, "tarefas")

# Saída esperada: Cada pessoa recebeu: tarefas