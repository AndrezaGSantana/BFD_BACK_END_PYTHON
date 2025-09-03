# I0dentificação de arquivo
arquivos = ('documento.pdf', 'foto.jpg', 'relatorio.pdf', 'planilha.xlsx')
contagem_pdf = sum(1 for arquivo in arquivos if arquivo.endswith('.pdf'))

print("Quantidade de arquivos PDF:", contagem_pdf)