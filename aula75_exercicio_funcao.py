'''
Exercício
Crie funções que duplicam, triplicam e quadriplicam o número recebido como parâmetro
'''
def multiplicador(vezes):
    def multiplicar(numero):
            return numero * vezes
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadriplicar = multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))