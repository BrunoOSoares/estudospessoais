"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""

hora_atual = input("Digite o horario atual: ")

try:
    hora_atual = int(hora_atual)

    if hora_atual >=0 and hora_atual <=11:
        print("Bom dia")
    elif hora_atual >=12 and hora_atual <=17:
        print("Boa tarde")
    elif hora_atual >=18 and hora_atual <=23:
        print("Boa noite")
    else:
        print("Horario desconhecido")
except:
    print("Insira um horario valido")