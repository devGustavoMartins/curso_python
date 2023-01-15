'''
Calculadora com while
'''
while True:
    input_1 = input('Digite um número: ')
    input_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+ - * /): ')

    num_validos = None

    try:
        num_1 = float(input_1)
        num_2 = float(input_2)
        num_validos = True
    except:
        num_validos = None

    if num_validos is None:
        print('Os números digitados não são válidos.')
        continue

    operadores_permitidos = '+-*/'
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    if len(operador) > 1:
        print('Somente um operador permitido.')
        continue

    if operador == '+':
        print(f'O resultado de {num_1} + {num_2} é = {num_1 + num_2:.2f}')
    elif operador == '-':
        print(f'O resultado de {num_1} - {num_2} é = {num_1 - num_2:.2f}')
    elif operador == '*':
        print(f'O resultado de {num_1} * {num_2} é = {num_1 * num_2:.2f}')
    elif operador == '/':
        print(f'O resultado de {num_1} / {num_2} é = {num_1 / num_2:.2f}')

    # Código para sair da calculadora
    sair = input('Quer sair? [s]Sim [n]Não ').lower().startswith('s')
    if sair is True:
        break