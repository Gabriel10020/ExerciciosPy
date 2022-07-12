def menu():
    print('\033[97m———' * 15)
    print(f'\033[97m{"MENU PRINCIPAL":^45}')
    print('\033[97m———\033[m' * 15)
    print('\033[93m1\033[97m - \033[94m Ver Pessoas Cadastradas')
    print('\033[93m2\033[97m - \033[94m Cadastrar nova Pessoa')
    print('\033[93m3\033[97m - \033[94m Sair Do Sistema')
    print('\033[97m———\033[m' * 15)
    c = 0
    opt = (1, 2, 3)
    while True:
        if c == 2:
            print('\033[97m———' * 15)
            print(f'\033[97m{"MENU PRINCIPAL":^45}')
            print('\033[97m———\033[m' * 15)
            print('\033[93m1\033[97m - \033[94m Ver Pessoas Cadastradas')
            print('\033[93m2\033[97m - \033[94m Cadastrar nova Pessoa')
            print('\033[93m3\033[97m - \033[94m Sair Do Sistema')
            print('\033[97m———\033[m' * 15)
            c = 0
        try:
            option = int(input('\033[92mSua Opção: \033[m'))
        except:
            print('\033[91mErro! Por favor digite um número inteiro válido.\033[m')
            c += 1
            continue
        else:
            if option not in opt:
                print(f'\033[91mErro! Por favor digite uma opção válida.')
                c += 1
                continue
            else:
                c = 0
                if option == 1:
                    print('\033[97m———' * 15)
                    print(f'\033[97m{"Opção 1":^45}')
                    print('\033[97m———' * 15)
                    continue
                elif option == 2:
                    print('\033[97m———' * 15)
                    print(f'\033[97m{"Opção 2":^45}')
                    print('\033[97m———' * 15)
                    continue
                elif option == 3:
                    print('\033[97m———' * 15)
                    print(f'\033[97m{"Saindo Do sistema... Até logo!":^45}')
                    print('\033[97m———' * 15)
                    break


# Programa principal:
vari = menu()
