from random import randint
numeros = []
def sorteia(num):
    for c in range(0, num):
        numeros.append(randint(1, 10))
    print('-=' * 20)
    print(f'Os números sorteados foram: {numeros}')

def soma(n):
    s = 0
    for c in n:
        if c % 2 == 0:
            s += c
    print('-=' * 20)
    print(f'A soma dos números pares sorteados foi: {s}')
    print('-=' * 20)


#Começando o programa:
sorteia(5)
soma(numeros)
