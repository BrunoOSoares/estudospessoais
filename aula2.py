nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')


if len(nome) != 0 and len(idade) != 0:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
   
    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome nao contem espaços')
        
    print(f'Seu nome contem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campo vazios.')