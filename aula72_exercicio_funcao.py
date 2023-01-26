# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.
def multiplicador(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
print(multiplicador(2, 4, 8))


# Crie uma função que fala se o número é par ou ímpar.
# Retorne se o número é par ou ímpar
def par_ou_impar(num=0):
    if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é ímpar')
par_ou_impar(8)