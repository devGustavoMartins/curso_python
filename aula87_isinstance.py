# isinstance -> saber se um objeto é de determinado tipo
lista = ['a', 1, 1.5, True, [0, 1, 2], (1, 2), {1, 2}, {'nome': 'Gustavo'}]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item)
    elif isinstance(item, str):
        print(item.upper())
    elif isinstance(item, (int, float)):
        print(item * 2)
    else:
        print(item, 'Outro')