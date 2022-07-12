n = int(input('Digite um número: '))
total = [n]
while True:
    continuar = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida, tente novamente.')
        continuar = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
    else:
        n = int(input('Digite um número: '))
        if n in total:
            print('Esse número já foi selecionado!')
        else:
            total.append(n)
totalsortiado = sorted(total)
print('-=' * 18)
print('Os números selecionados foram: ', end='')
for c in totalsortiado:
    print(c, end=' ')
print('\nFim.')