# ESSA AULA FOI UM DESAFIO PARA INDICAR CASO UM NÚMERO SEJA MAIOR, IGUAL OU MENOR DO QUE OUTRO
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

int_primeiro = int(primeiro_valor)
int_segundo = int(segundo_valor)

if int_primeiro == int_segundo:
    print(f'{int_primeiro} é igual {int_segundo}')
elif int_primeiro > int_segundo:
    print(f'{int_primeiro} é maior do que {int_segundo}')
elif int_primeiro < int_segundo:
    print(f'{int_primeiro} é menor do que {int_segundo}')