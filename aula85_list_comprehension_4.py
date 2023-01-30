# As duas primeiras formas de fazer lista darão o mesmo
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
# print(lista)

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
# print(lista)

lista = [
    [letra for letra in 'Gustavo']
    for x in range(3)
]
print(lista)