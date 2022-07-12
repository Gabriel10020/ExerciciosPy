def contador(i, f, p):
    print('-=' * 20)
    if i < f:
        count = i
        while count <= f:
            if p > 0:
                print(f'{count}', end=' ')
                count += p
            elif p == 0:
                print(f'{count}', end=' ')
                count += 1
        print('Fim')
    else:
        count = i
        while count >= f:
            if p > 0:
                print(f'{count}', end=' ')
                count -= p
            elif p < 0:
                print(f'{count}', end=' ')
                count += p
            elif p == 0:
                print(f'{count}', end=' ')
                count += 1
        print('Fim')
    print('')



#inicio do programa:
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
contador(int(input('Digite o Inicio: ')), int(input('Digite o fim da lista: ')), int(input('Digite a progressão: ')))
