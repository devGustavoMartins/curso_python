"""
Closure e funções que retornam outras funções
"""
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

dia = criar_saudacao('Bom dia')
tarde = criar_saudacao('Boa tarde')
noite = criar_saudacao('Boa noite')

for nome in ['Gustavo', 'Sophia']:
    print(dia(nome))
print()
for nome in ['Enrico', 'Pedro']:
    print(tarde(nome))
print()
for nome in ['Gustavo', 'Sophia']:
    print(noite(nome))
print()