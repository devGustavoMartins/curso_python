'''
Listas de listas e seus índices
'''
salas = [
    # 0        1
    ['Gustavo', 'Martins', ],  # 0
    # 0
    ['Sophia', 'Franchi'],  # 1
    # 0         1           2
    ['Enrico', 'Sequinel', 'Marcassa', ],  # 2
]

# print(salas[0][1])

for sala in salas:
    for aluno in sala:
        print(aluno, end=' ')
    print('\n')