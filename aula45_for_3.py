"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# for letra in texto
texto = 'Gustavo'  # iterável
iterador = iter(texto)  # iterador

# O que acontece ao utilizar o FOR
while True:
    try:
        print(next(iterador))
    except StopIteration:
        break

# Utilizando o for, o código fica muito mais simples e compacto dando o mesmo resultado
for letra in texto:
    print(letra)