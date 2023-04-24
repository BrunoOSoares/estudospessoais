#Escreva um programa que mostre os números de 1 até o numero digitado pelo usuário, mas,
#apenas os números múltiplos de 3.

num = 0

num_digitado = int(input("Digite o numero para que seja feito a contagem ate o numero informado: "))

while num <= num_digitado:
    if num / 3 and num % 3 == 0:
        print(num)
    num += 1
