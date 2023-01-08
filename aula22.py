# AULA SOBRE OPERADOR LÓGICO OR
'''
and (e) or (ou) not (não)
and - Todas as condições precisam ser verdadeiras. Se qualquer valor for falso, tudo será considerado como falso.
São considerados falsy: Vistos até agora -> (0 / 0.0 / '' / False)
Também existe o tipo None, que é usado para representar um não valor.
'''

a = 0
b = 1
c = 0

if a or b or c:
    print('Algum bool é verdadeiro')