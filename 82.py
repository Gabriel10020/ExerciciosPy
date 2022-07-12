lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print('-=' * 30)
print(f'A lista dos números ficou: {lista}')
print(f'A lista dos pares ficou: {par}')
print(f'E a dos impares ficou: {impar}')
