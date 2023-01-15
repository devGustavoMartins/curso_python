'''
while/else
-> Ao usar a função break, o else após o while não é executado.
'''
string = 'Gustavo Martins'
i = 0
while i < len(string):
    letra = string[i]

    if(letra == ' '):
        break

    print(letra, end='')
    i += 1
else:
    print('\nNão tem espaço nessa string.')

if(' ' in string):
    print('\nTem espaço na string.')