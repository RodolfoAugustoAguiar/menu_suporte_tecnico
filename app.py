# Menu do laboratório e do suporte técnico
# Autor: Rodolfo Augusto Aguiar

import os

os.system('cls')

print ("Menu do Laboratório")
print("Opções: ")
print("1 - Listar computadores disponíveis")
print("2 - Abrir chamado de manutenção")
print("3 - Ver regras de uso do laboratório")

opcao1 = input("Digite uma opção (1 - PCs, 2 - Manutenção, 3 - Regras): ")

match opcao1:
    case "1" | "um" | "Um" | "UM":
        print("Computadores disponíveis: Lab01-PC01 ao Lab01-PC20.")
    case "2" | "dois" | "Dois" | "DOIS":
        print("Abrindo chamado de manutenção... descreva o problema.")
        print("Menu de Suporte Técnico")
        print("Opções: ")
        print("P: Pedido pendente")
        print("E: Pedido enviado")
        print("C: Pedido cancelado")
        opcao2 = input("Digite a opção (P, E ou C): ").upper()
        match opcao2:
            case "P":
                print("Seu pedido está Pendente e em processamento.")
            case "E":
                print("Seu pedido já foi Enviado! Verifique seu e-mail.")
            case "C":
                print("Seu pedido foi Cancelado. Entre em contato com o RH.")
            case _:
                print("Opção inválida. Tente novamente.")
    case "3" | "três" | "Três" | "TRêS":
        print("Regras: uso individual, silêncio e não alterar configurações.")
    case _:
        print("Opção inválida. Tente novamente.")
