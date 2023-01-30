# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de iteráveis.
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# Filtragem de dados no list comprehension
produtos = [
    {'nome': 'p1', 'preço': 10, },
    {'nome': 'p2', 'preço': 20, },
    {'nome': 'p3', 'preço': 30, },
    {'nome': 'p4', 'preço': 15, },
    {'nome': 'p5', 'preço': 5, },
    {'nome': 'p6', 'preço': 7.5, },
]
novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.5}
    if produto['preço'] < 20 else {**produto}
    for produto in produtos
    if produto['preço'] > 10
]
p(novos_produtos)

# lista = [
#     n 
#     for n in range(10)
#     if n <= 5 and n > 0
# ]
# p(lista)