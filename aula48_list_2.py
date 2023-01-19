"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
print('Antes da alteração ', end='')
lista = [0, 10, 20, 30, 40]
print(lista)
print('Após a alteração ', end='')
del lista[0]  # Deleta na posição definida
lista.append(50)  # Append vai adicionar no final da lista
lista.append(60)  # Append vai adicionar no final da lista
lista.append(70)  # Append vai adicionar no final da lista
lista.append(80)  # Append vai adicionar no final da lista
lista.append(90)  # Append vai adicionar no final da lista
lista.append(100)  # Append vai adicionar no final da lista
lista.append('Último valor da lista')  # Append vai adicionar no final da lista
lista.pop()  # Pop retira o último valor da lista
print(lista)