# AULA SOBRE ORDEM DAS OPERAÇÕES MATEMÁTICAS NO PYTHON
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

# Portanto, a primeira conta a ser executada são os Parênteses, de dentro pra fora, EX: (Terceiro(Segundo(Primeiro))). 
# Depois a Exponenciação.
# Depois as operações como Multiplicação, Divisão, Divisão Inteira e Módulo. 
# Por fim a Adição e Subtração são feitas.
conta_1 = 1 + 1 ** 5 + 5
print(conta_1)

conta_2 = (1 + 1) ** (5 + 5)
print(conta_2)