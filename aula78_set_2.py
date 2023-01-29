# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

# Sets são eficientes para remover valores duplicados de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# l1 = [1, 2, 3, 3, 4, 3, 4, 4, 5, 1, 2]
# s1 = set(l1)
# l2 = list[s1]
# print(l2)

s1 = {1, 2, 2, 1, 1, 3, 3, 3}

for numero in s1:
    print(numero)
print(s1)
