# Entrada de dados
cor = input("Digite a cor do semáforo (verde, amarelo, vermelho): ")

match cor:
    case "verde":
        print("Pode seguir.")
    case "amarelo":
        print("Atenção! Reduza a velocidade.")
    case "vermelho":
        print("Pare imediatamente.")
    case _:
        print("Cor inválida!")