try:
    n = int(input('Digite um número inteiro: '))
except:
    print('Parece que tivemos um problema. Vamos tentar novamente.')
    while True:
        n = str(input('Digite um número inteiro: '))
        if n.isnumeric() == True:
            n = int(n)
            break
        print('Parece que tivemos um problema. Vamos tentar novamente.')
    print(f'O número digitado foi {n}')
else:
    print(f'O número digitado foi {n}')
