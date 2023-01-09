"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
n = len(nome)
nome_formatado = nome.title()

if(nome and idade != False):
    print(f'Seu nome é {nome_formatado}')
    print(f'Seu nome invertido é {nome_formatado[::-1]}')
    
    if(' ' in nome_formatado):
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {n - 1} letras')
    print(f'A primeira letra do seu nome é {nome_formatado[0]}')
    print(f'A última letra do seu nome é {nome_formatado[-1]}')
elif(nome and idade == False):
    print('Desculpe, você deixou campos vazios.')