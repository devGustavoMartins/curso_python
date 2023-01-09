# INTERPOLAÇÃO BÁSICA DE STRINGS
'''
s - string
d e i - int
f - float
 x e X - Hexadecimal (ABCDEF0123456789)
'''

nome = 'Gustavo'
preco = 1000.97361298
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))