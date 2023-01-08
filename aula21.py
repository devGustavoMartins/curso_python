# AULA SOBRE OPERADOR LÓGICO AND
'''
and (e) or (ou) not (não)
and - Todas as condições precisam ser verdadeiras. Se qualquer valor for falso, tudo será considerado como falso.
São considerados falsy: Vistos até agora -> (0 / 0.0 / '' / False)
Também existe o tipo None, que é usado para representar um não valor.
'''

a = 1
b = 0
c = 1

if a == 1 and b == 1 and c == 1:
    print('Tudo vale um!')
else:
    print('Algo está errado')