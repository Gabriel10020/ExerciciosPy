from random import randint
n = (randint(1, 999), randint(1, 999), randint(1, 999), randint(1, 999), randint(1, 999))
ordem = sorted(n)
print(f'A lista de números gerados foram: {n}')
print(f'O maior valor foi {ordem[0]} e o menor {ordem[-1]}')