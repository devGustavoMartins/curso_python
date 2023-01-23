"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
def soma(x, y):
    print(x + y)

soma(1, 2)
soma(x=1, y=2)
soma(1, y=2)  # É possível utilizar argumentos posicionais antes de argumentos nomeados
# soma(x=1, 2)  Não pode usar argumentos posicionais após argumentos nomeados