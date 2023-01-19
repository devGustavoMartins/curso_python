'''
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.
'''
import os
lista = []

while True:
    opcao = input('Selecione uma opção\n[I] Inserir [A] Apagar [L] Listar: ').capitalize()
    
    if opcao == 'I':
        inserir_produto = input('Digite o que você deseja adicionar na lista: ').capitalize()
        lista.append(inserir_produto)
        os.system('cls')
        print(f'Você adicionou {inserir_produto} na lista.')

    elif opcao == 'A':
        apagar_indice = input('Escolha o índice para apagar: ')
        
        try:
            indice = int(apagar_indice)
        except:
            os.system('cls')
            print('Não digitou um número.')
            continue

        try:
            del lista[indice]
            os.system('cls')
            print(f'Você apagou o índice {indice}')
        except:
            os.system('cls')
            print('Não foi possível apagar esse índice')
            continue

    elif opcao == 'L':
        os.system('cls')
        if len(lista) != 0:
            for indice, produto in enumerate(lista):
                print(indice, produto)
        else:
            os.system('cls')
            print('Nada para listar')
            continue

    else:
        os.system('cls')
        print('Escolheu uma opção indisponível!')
        continue