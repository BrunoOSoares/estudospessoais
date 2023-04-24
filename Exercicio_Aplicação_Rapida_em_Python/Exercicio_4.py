#Escreva um programa que mostre os números de 1 até um numero digitado pelo usuário, mas,
#apenas os números impares.

num = 0

num_digitado = int(input("Informa o numero para a contagem de 1 ate o numero informado: "))

while num <= num_digitado:
    if num % 2 != 0:
        print(num)
    num +=1