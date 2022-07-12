lista = []
n = int(input('Digite um número: '))
lista.append(n)
continuar = ''
while True:
    while True:
        if continuar in 'SN':
            break
        print('Opção inválida, tente novamente!')
        continuar = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
    elif continuar == 'S':
        n = int(input('Digite um número: '))
        lista.append(n)
    continuar = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
print('A lista de números é: ', end='')
lista.sort(reverse = True)
for c in lista:
    print(c, end=', ')
print(f'\nA lista contém {len(lista)} termos.')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista')
