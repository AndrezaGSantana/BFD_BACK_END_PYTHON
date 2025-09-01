# Entrada de dados
nota = int(input("Digite uma nota de 1 a 5: "))

match nota:
    case 1:
        print("Muito ruim")
    case 2:
        print("Ruim")
    case 3:
        print("Regular")
    case 4:
        print("Bom")
    case 5:
        print("Excelente!")
    case _:
        print("Erro: nota fora do intervalo (1 a 5).")