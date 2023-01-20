'''
split e join com list e str
split -> divide uma string
join -> une uma string
'''
frase = 'Vou separar essa frase palavra por palavra'
lista_palavras = frase.split()

for i, palavra in enumerate(lista_palavras):
    print(i, palavra)

palavras_unidas = '-'.join(lista_palavras)
print(palavras_unidas)