# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer outra em Python. 
# Porém, são funções anônimas que contém apenas uma linha. 
# Ou seja, tudo deve ser contido dentro de uma única expressão.
lista = [
    {'nome': 'Gustavo', 'sobrenome': 'Martins'},
    {'nome': 'Sophia', 'sobrenome': 'Franchi'},
    {'nome': 'Enrico', 'sobrenome': 'Marcassa'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])  # Mesmo funcionamento que a função acima
l2 = sorted(lista, key=lambda item: item['sobrenome'])

print('Nomes em ordem'); exibir(l1)
print('Sobrenomes em ordem'); exibir(l2)