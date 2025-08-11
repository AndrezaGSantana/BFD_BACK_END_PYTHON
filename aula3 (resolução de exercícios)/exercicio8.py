import datetime

hora_atual = datetime.datetime.now()
# Ausência do "_" 

nome_usuario = input("Digite o seu nome: ")
# Uso de "!" e ausência de ""

print(f'Olá, {nome_usuario}!Agora são {hora_atual.strftime("%H:%M")} horas.')
