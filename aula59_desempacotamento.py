# Desempacotamento em chamadas de métodos e funções

string = 'Gustavo'
lista = ['Gustavo', 'Sophia', 'Enrico']
tupla = 'Gustavo', 'de', 'Oliveira', 'Martins'

# a, *resto, c = lista
# print(a, c)

print(*lista)
print(*string)
print(*tupla)