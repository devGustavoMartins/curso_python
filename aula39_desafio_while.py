'''
Iterando strings com while
O desafio dessa aula foi fazer uma string nova adicionando * em cada
'''
#       0123456789...
nome = 'Gustavo Martins' # Iteráveis
#         ...-987654321

indice = 0

while indice < len(nome):
    print(f'*{nome[indice]}', end='')
    indice += 1