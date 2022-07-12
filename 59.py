n1 = int(input('\033[96mDigite um valor: '))
n2 = int(input('Digite outro valor: '))
escolha = 0
while escolha != 5:
    print('\033[95m-=' * 18)
    print('\033[97m[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior número\n'
          '[4] Novos números\n'
          '[5] Sair do programa.')
    print('\033[95m-=' * 18)
    escolha = int(input('\033[93mO que deseja fazer? Digite aqui: '))
    print('\033[95m-=' * 18)
    if escolha == 1:
        soma = n1 + n2
        print(f'\033[94mA soma entre {n1} e {n2} é {soma}')
    elif escolha == 2:
        multi = n1 * n2
        print(f'\033[94mA multiplicação de {n1} e {n2} fica {multi}')
    elif escolha == 3:
        if n1 > n2:
            print(f'\033[94m{n1} é o maior número.')
        elif n2 > n1:
            print(f'\033[94m{n2} é o maior número.')
    elif escolha == 4:
        n1 = int(input('\033[96mDigite um valor: '))
        n2 = int(input('\033[96mDigite outro valor: '))
    elif escolha == 5:
        print('\033[91mFinalizando o programa...')
    else:
        print('\033[31mEscolha inválida, tente novamente. ')
