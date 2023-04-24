#Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo,
#assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado.
#Lembrese de que podemos entender o quociente da divisão de dois números como a quantidade de vezes
#que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes
#de 20.

# lê os dois números
dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

# inicializa as variáveis de controle
quociente = 0
resto = dividendo

# realiza a divisão utilizando apenas soma e subtração
while resto >= divisor:
    resto = resto - divisor
    quociente = quociente + 1

# exibe o resultado
print("Divisão inteira:", quociente)
print("Resto da divisão:", resto)
