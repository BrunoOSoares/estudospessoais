"""
Faça um programa que peça ao usuario para digirar um numero inteiro,
informe se este numero é par ou impar. Caso o usuario não digite um numero
inteiro, informe que não é um numero inteiro.
"""

num_int = (input("Digite um numero inteiro: "))

if num_int.isdigit():
    num_int = int(num_int)     
    if num_int % 2 == 0:
        print(f"O numero {num_int} é par")
    else:
        print(f"O numero {num_int} é impar")   
else:
    print("O numero digitado não é um inteiro")