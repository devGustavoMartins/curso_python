# OPERADORES IN E NOT IN
'''
Strings são iteráveis.
  0 1 2 3 4 5 6
  G u s t a v o
  7 6 5 4 3 2 1
'''

'''
# Vai printar Gustavo, uma letra por linha usando valores positivos
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])
print(nome[5])
print(nome[6])
print()
# Também vai printar Gustavo, uma letra por linha usando valores negativos
print(nome[-7])
print(nome[-6])
print(nome[-5])
print(nome[-4])
print(nome[-3])
print(nome[-2])
print(nome[-1])
'''

'''
nome = 'Gustavo'
print('H' in nome) # Vai buscar a letra 'H' dentro de 'Gustavo' e retornar um bool, caso tenha retorna True. Nesse exemplo retorna False.
print('H' not in nome) # Vai buscar a letra 'H' dentro de 'Gustavo e retornar um bool, caso não tenha retorna True. Nesse exemplo retorna True.
'''

nome = input('Digite o seu nome: ')
encontrar = input('Digite uma letra: ')

if(encontrar in nome):
    print(f'Seu nome é {nome} e a letra "{encontrar}" está presente nele!')
else:
    print(f'Seu nome é {nome} e a letra "{encontrar}" não está presente nele!')