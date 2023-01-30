# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de iteráveis.

# print(list(range(10)))

# lista = []
# for numero in range(10):
#     lista.append(numero)
# # print(lista)

lista = [
    (numero + 1) * 2
    for numero in range(10)
]
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preço': 10, },
    {'nome': 'p2', 'preço': 20, },
    {'nome': 'p3', 'preço': 30, },
    {'nome': 'p4', 'preço': 15, },
]
novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.5}
    if produto['preço'] < 20 else {**produto}
    for produto in produtos
]
print(*novos_produtos, sep='\n')