# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Gustavo')  # Adiciona um elemento inteiro
s1.update('Martins')  # Adiciona letra por letra
s1.update((1, 2, 3, 4))  # Dessa forma é possível adicionar mais de um elemento com a tupla
print(s1)

s1.discard('Gustavo')  # Remove o elemento definido
print(s1)

s1.clear()  # Limpa o set
print(s1)