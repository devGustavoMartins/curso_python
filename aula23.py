# OPERADOR LÓGICO NOT
'''
Usado para inverter expressões.
not True = False.
not False = True
'''

senha = input('Senha: ')
if senha != '123456':
    print('Senha incorreta')
else:
    print('Entrou')

print(not 0)
print(not True)