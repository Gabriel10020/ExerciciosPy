from random import randint
from time import sleep
print('===' * 15)
print(f'               Jogo Da Sena')
print('===' * 15)
lista = list()
temp = list()
num = 0
n = int(input('Quantos jogos deseja sortear? '))
for v in range(0, n):
    temp.clear()
    for c in range(0, 6):
        num = randint(1, 60)
        while num in temp:
            num = randint(1, 60)
        temp.append(num)
    temp.sort()
    lista.append(temp[:])
for e, l in enumerate(lista):
    print(f'O {e + 1}º jogo sorteado foi {l}')
    sleep(1)