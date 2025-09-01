# Entrada de dados
status = input("Digite o status do pedido (recebido, em_preparação, em_entrega, entregue): ")

match status:
    case "recebido":
        print("Seu pedido foi recebido e está sendo processado.")
    case "em_preparação":
        print("Seu pedido está em preparação.")
    case "em_entrega":
        print("Seu pedido está a caminho!")
    case "entregue":
        print("Seu pedido foi entregue. Bom apetite!")
    case _:
        print("Status não identificado.")