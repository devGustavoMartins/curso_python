# NA AULA 7 HÁ A INTRODUÇÃO DE VARIÁVEIS
'''
Variáveis são usadas para salvar algo na memória do computador.
PEP8: inicie variáveis com letra minúsculas, pode usar números e underline.
O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a um nome (variável)
Uso = nome_variavel = expressão
'''

nome = 'Gustavo'
idade = 16
maior_de_idade = idade >= 18

print('Nome: ', nome)
print('Idade: ', idade)

if(maior_de_idade == True): 
    print('É maior de idade')
if(maior_de_idade == False):
    print('É menor de idade')