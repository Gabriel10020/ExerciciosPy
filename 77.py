palavras = ('Macaco', 'Bike', 'Moto', 'Chaveiro', 'Marcos', 'Mimica',
            'Melancia', 'zebra', 'Bigorna', 'futuro')
vogais = 'aeiou'
for c in palavras:
    print(f'\nAs vogais da palavra {c.upper()} são: ', end='')
    for letra in c:
        if letra in vogais:
            print(f'{letra}', end=' ')
