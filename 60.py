from math import factorial
n = int(input('Digite um número: '))
fac = factorial(n)
c = n
while c > 0:
    print(f'{c}', end='')
    if c > 0:
        print('x')
    c -= 1
print(f' = {fac}')
