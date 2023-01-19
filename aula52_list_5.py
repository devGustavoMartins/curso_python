"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Gustavo', 'Sophia']
lista_b = lista_a

lista_a[1] = 'Enrico'
print(lista_b)
