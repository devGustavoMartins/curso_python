# Empacotamento e desempacotamento de dicionários

# a, b = 1, 2
# a, b = b, a
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

pessoa = {
    'nome': 'Gustavo',
    'sobrenome': 'Martins',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.8,
}

pessoa_completa = {**pessoa, **dados_pessoa}

'''
args e kwargs
args (já vi)
kwargs -> keyword arguments (argumentos nomeados)
'''
def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)
    print()

mostro_argumentos_nomeados(1, 2, 3, nome='Gustavo', idade=16)
mostro_argumentos_nomeados(**pessoa_completa)