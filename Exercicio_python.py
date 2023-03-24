import random
#Este programa solicita ao usuario qual operação ele quer fazer , o programa vai mostrar um teste e o usuario escolhe a resposta.
#o programa vai mostrar se está correto ou não

numero1 = random.randrange(1,20)
numero2 = random.randrange(1,20)
numerodiv1 = random.randrange(2,20,2)
numerodiv2 = random.randrange(2,10,2)
tentativa = 0
 
print('---------------- MATEMATICAMENTE GAME---------------\n')
print('----------------  FACIL = SOMA E SUB ---------------')
print('----------------   MEDIO = MULT --------------------')
print('----------------   DIFICIL = DIV -------------------\n')
operacao = input('Escolha uma operação matematica (soma),(sub),(mult),(div) : ')

if operacao == 'soma':
    soma = numero1 + numero2  
    print(f"O teste é a soma de {numero1} + {numero2}")
    resultado = int(input("Digite o resultado do teste: "))
    
    while tentativa < 3:
        tentativa += 1
        if resultado == soma:
            print("Você acertou o teste!")
            break
        else:
            print("Você errou o teste!")
            tentativa += 1
            resultado = int(input("Digite o resultado do teste: "))
              
       
    
elif operacao == 'sub':  
    sub = numero1 - numero2
    print(f"O teste é a subtração de {numero1} - {numero2}")
    resultado = int(input("Digite o resultado do teste: "))
    
    while tentativa < 3:
        tentativa += 1
        if resultado == sub:
            print("Você acertou o teste!")
            break
        else:
            print("Você errou o teste!")
            tentativa += 1
            resultado = int(input("Digite o resultado do teste: "))
    
    
elif operacao == 'mult': 
    mult = numero1 * numero2
    print(f"O teste é a multiplicação de {numero1} * {numero2}")
    resultado = int(input("Digite o resultado do teste: "))
    
    while tentativa < 3:
        tentativa += 1
        if resultado == mult:
            print("Você acertou o teste!")
            break
        else:
            print("Você errou o teste!")
            tentativa += 1
            resultado = int(input("Digite o resultado do teste: "))
        
    
elif operacao == 'div':
    div = numerodiv1 / numerodiv2
    print(f"O teste é a divisão de {numerodiv1} / {numerodiv2}")
    resultado = float(input("Digite o resultado do teste: "))
    
    while tentativa < 3:
        tentativa += 1
        if resultado == div:
            print("Você acertou o teste!")
            break
        else:
            print("Você errou o teste!")
            tentativa += 1
            resultado = float(input("Digite o resultado do teste: "))
                        
if tentativa > 3:
    print("Acabou suas chances :(")   
    

    
    
    

    