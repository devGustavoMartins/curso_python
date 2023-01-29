def executa(funcao, *args):
    return funcao(*args)

# def soma(x, y):
#     return x + y

# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

duplica = executa(lambda m: lambda n: n * m, 2)
triplica = executa(lambda m: lambda n: n * m, 3)
quadriplica = executa(lambda m: lambda n: n * m, 4)

print(executa(lambda x, y: x + y, 2, 3))  # Soma

print(duplica(6))
print(triplica(5))
print(quadriplica(6))