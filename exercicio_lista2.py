'''
Faça uma lista de comprar com listas
O usuario deve ter a possibilidade de
inserir,apagar e listar valores da sua lista
não permita que o programa quebre com 
erros de indices inexistentes na lista.
'''
import os

lista = []
item = ""
while True:
    operacao = 'ial'
    
    
    escolha = input("Selecione uma opção: [i]inserir [a]apagar e [l]listar: \n")
    
    if len(escolha) > 1:
        print("Digite apenas uma letra para opção desejada: \n")
        continue
    
    if  escolha not in operacao:
        print("Escolha a operação correta: [i]inserir [a]apagar e [l]listar: \n")
        continue
    
    if escolha == 'i':
        os.system('cls')
        item = input("Digita o valor para inserir na lista de compras: ")
        lista.append(item)
        print(f"O item {item} foi adicionado")
        continue
    
    if escolha == 'a' and item not in lista:
        print("A lista está vazia!!!")
        continue
    
    if escolha == 'a':
        os.system('cls')
        try:
            apagar = input('Escolha a compra que deseja apagar: ')
            del lista[int(apagar)]
        except: 
            print('Escolha um item conforme lista de compras')   
        continue
    
    if escolha == 'l' and item in lista:
        os.system('cls')
        for i, valor in enumerate(lista, start=1):
            print(i,valor)
        continue
    else:
        print("A lista está vazia!!!")
        continue
        
    