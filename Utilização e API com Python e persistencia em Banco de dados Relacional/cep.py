import requests
import mysql.connector


cep = input("Digite o seu CEP: ")
link = f"https://viacep.com.br/ws/{cep}/json/"
requisicao = requests.get(link)
dados = requisicao.json()


print(dados)


conexao = mysql.connector.connect(
    host="localhost",
    user="root",          
    password="Nemessis25#",
    database="viacep"
)
print(conexao)
cursor = conexao.cursor()
print("Conectado com o banco")
sql = """
INSERT INTO enderecos (cep, logradouro, bairro, localidade, uf)
VALUES (%s, %s, %s, %s, %s)
"""


valores = (
    dados.get("cep"),
    dados.get("logradouro"),
    dados.get("bairro"),
    dados.get("localidade"),
    dados.get("uf")
)


cursor.execute(sql, valores)
conexao.commit()


print("Endereço inserido com sucesso no MySQL!")


cursor.close()
conexao.close()