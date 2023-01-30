# Dictionary comprehension e set comprehension
produto = {
    'nome': 'caneta preta',
    'preço': 2,
    'categoria': 'escola', 
}
# for chave, valor in produto.items():
#     print(chave, valor)

d1 = {
    chave.title(): valor.title()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}
print(d1)


s1 = {
    i + 1
    for i in range(10)
    if i < 5
}
print(s1)