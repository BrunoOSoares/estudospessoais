### calculadora
 
while True:

# entrada dos numeros e escolha do operador
    
     num1 = input("Digite um numero: ")
     num2 = input("Digite um segundo numero: ")
     operador = input("Escolha o operador: + - * / : ")
     
     numeros_validos = None
     num1_float = 0
     num2_float = 0
     
     try:
         num1_float = float(num1)
         num2_float = float(num2)
         numeros_validos = True
     except:
         numeros_validos = None
         
     if numeros_validos is None:
        print("numeros invalidos")
        continue 
         
     operadores = "+-*/"
        
        
     if operador not in operadores:
             print("O operador escolhido não é valido")
             continue
         
     if operador == '+':
        print(f"A soma dos numeros {num1_float} + {num2_float} é = ", num1_float + num2_float)
     elif operador == '-':
        print(f"A subtração dos numeros {num1_float} - {num2_float} é = ", num1_float - num2_float)
     elif operador == '*':
        print(f"A multiplicação dos numeros {num1_float} * {num2_float} é = ", num1_float * num2_float)
     elif operador == '/':
        print(f"A divisão dos numeros {num1_float} / {num2_float} é = ", num1_float / num2_float)
     else:
        print("Digite apenas numeros e operações validas")
         
      
     sair = input("Deseja sair? Sim[s]").lower().startswith('s')
     if sair is True:
        break