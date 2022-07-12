n = num = 0
while True:
    n = int(input('Digite um número para a tabuada: '))
    if n < 0:
        break
    else:
        for c in range(1, 11):
            print(f'{n} x {c} = {c * n}')
print('Fim.')