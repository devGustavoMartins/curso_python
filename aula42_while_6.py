'''
Aula utilizando while para saber qual letra repetiu mais em uma frase
'''
frase = 'Gustavo de Oliveira Martins'

i = 0
apareceu_mais_qtd = 0
letra_mais_qtd = ''
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i+=1
        continue
    qtd_letra_atual = frase.count(letra_atual)

    if apareceu_mais_qtd < qtd_letra_atual:
        apareceu_mais_qtd = qtd_letra_atual
        letra_mais_qtd = letra_atual.capitalize()
    i+=1
print(f'A letra que mais apareceu foi "{letra_mais_qtd}", a qual apareceu {apareceu_mais_qtd} vezes')