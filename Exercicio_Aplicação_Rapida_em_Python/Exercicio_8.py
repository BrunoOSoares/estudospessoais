#Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro
#pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de
#que podemos entender a multiplicação de dois números como a soma sucessivas de um deles. Assim, 4 x 5
#= 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4. 

# leitura dos números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# variável para armazenar o resultado da multiplicação
resultado = 0

# loop para somar num1, num2 vezes
for i in range(num2):
    resultado += num1

# impressão do resultado
print("O resultado da multiplicação é:", resultado)