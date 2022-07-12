valores = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')),
           int(input('Digite um valor: ')))
nove = valores.count(9)
pares = 0
print('-=' * 20)
print(f'O numero 9 apareceu {nove} vezes.')
if 3 in valores:
    trespos = valores.index(3)
    print(f'O número 3 apareceu na {trespos + 1}º posição')
else:
    print('O número 3 não apareceu na lista.')
print('Os números pares foram: ', end=' ')
for c in valores:
    if c % 2 == 0:
        print(f'{c} ', end='')
print('\n')
print('-=' * 20)
