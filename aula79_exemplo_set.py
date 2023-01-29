# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())

    if 'g' in letras:
        print('Acabou!')
        break
    print(letras)