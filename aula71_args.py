"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembrar do desempacotamento

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

numeros = [1, 2, 3, 4, 5, 6, 10]
print(soma(1, 2, 3, 4, 5, 6, 10))
print(sum(numeros))  # Função do python