"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
cpf = '746.824.890-70'
cpf_validar = cpf.replace('.', '').replace(' ','').replace('-', '')
novo_cpf = []
multiplicador = 10
soma = 0
limitador = 0

for digito in cpf:  # Deixa somente os dígitos no cpf, gerando um novo cpf
    if digito == '-':
        break
    if digito == '.':
        ...
    else:       
        digito = int(digito)
        digito *= multiplicador
        novo_cpf.append(digito)
        multiplicador -= 1

for numero in novo_cpf:
    soma += numero

soma *= 10
soma %= 11
digito_1 = 0 if soma > 9 else soma

novo_cpf = []
limitador = 0
multiplicador = 11
soma = 0

for digito in cpf:  # Deixa somente os dígitos no cpf, gerando um novo cpf
    if limitador == 10:
        break
    if digito == '.' or digito == '-':
        ...
    else:
        limitador += 1
        digito = int(digito)
        digito *= multiplicador
        novo_cpf.append(digito)
        multiplicador -= 1


for numero in novo_cpf:
    soma += numero

soma *= 10
soma %= 11
digito_2 = 0 if soma > 9 else soma


nove_digitos = cpf_validar
cpf_gerado = f'{nove_digitos[:9]}{digito_1}{digito_2}'


if cpf_validar == cpf_gerado:
    print(f'{cpf} é válido')
else:
    print('CPF inválido')