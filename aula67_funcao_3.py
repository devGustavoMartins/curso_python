'''
Valores padrão para parâmetros.
Ao definir uma função, os parâmetros podem ter valores padrão. Caso o valor não seja enviado para o parâmetro, o valor padrão será utilizado.
Refatorar: editar o seu código.
'''

def soma(x, y, z=None):
    print(x + y + z)

soma(1, 2, 7)
soma(21, 53, 26)
soma(451, 549)