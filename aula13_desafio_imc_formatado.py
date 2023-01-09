# CÓPIA DO EXERCÍCIO ANTERIOR, PORÉM DANDO UM EXEMPLO DE FORMATAÇÃO DE STRING
nome = 'Gustavo Martins'
altura = 1.8
peso = 60
imc = peso / (altura * altura)

print(f'{nome} tem {altura}m de altura, pesa {peso}kg e seu IMC é {imc:.2f}')  # Utilizando formatação de string
print(nome, ' tem ', altura, 'm de altura, pesa ', peso, 'kg e seu IMC é ', imc, sep='')  # Utilizando a forma padrão da string