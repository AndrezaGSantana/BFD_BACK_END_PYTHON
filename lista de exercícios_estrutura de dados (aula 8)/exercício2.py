# Entrada de dados
alunos = ['Bruno', 'Ana', 'Carlos', 'Denise', 'Felipe']

# Ordenando em ordem decrescente
alunos.sort(reverse=True)
print("Alunos em ordem decrescente:", alunos)

# Acessando os alunos 'Felipe' e 'Ana' pelas posições
pos_felipe = alunos.index('Felipe')
pos_ana = alunos.index('Ana')

print(f"Aluno na posição {pos_felipe}: {alunos[pos_felipe]}")
print(f"Aluno na posição {pos_ana}: {alunos[pos_ana]}")