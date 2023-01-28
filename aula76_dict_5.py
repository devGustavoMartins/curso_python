# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    'nome': 'Gustavo',
    'sobrenome': 'Martins',
    'idade': 16,
    'altura': 1.8,
}

# print(p1.get('nome'))

# sobrenome = p1.pop('sobrenome')
# print(sobrenome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

p1.update({
    'nome': 'Sophia',
    'sobrenome': 'Franchi',
    'idade': 17,
    'altura': 1.6
})
print(p1)