# Manipulando chaves e valores em dicionários
pessoa = {}

pessoa['nome'] = 'Gustavo'
pessoa['sobrenome'] = 'Martins'
pessoa['idade'] = 16
pessoa['altura'] = 1.8

pessoa['endereço'] = {'rua': 'tal tal', 'número': 123}

del pessoa['endereço']

for caracteristica in pessoa:
    print(caracteristica.title(), pessoa[caracteristica])