#– Escreva um programa que exiba a tabuada do número digitado de 0 a 10.

tabuada = 0
num = 0
num_digitado = int(input('Informe o numero para a tabuada: '))

mult = num * num_digitado

while tabuada <= 10 and num <=10:
    print(f'{num} x {num_digitado} = {mult}')
    num += 1
    mult = num * num_digitado
tabuada += 1
    