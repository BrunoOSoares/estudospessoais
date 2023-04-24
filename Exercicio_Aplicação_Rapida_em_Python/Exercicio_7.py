#– Escreva um programa que exiba a tabuada do número digitado, onde o usuário possa escolher o
#inicio e o fim da tabuada. 


num = int(input('Digite o numero inicial: '))
tabuada = int(input('Digite qual a tabuada desejada: '))
num_final = int(input('Digite o numero final da tabuada: '))
mult = num * tabuada

for i in range(num_final):
    print(f'{num} x {tabuada} = {mult}')
    num +=1
    mult = num * tabuada
    
    
    
