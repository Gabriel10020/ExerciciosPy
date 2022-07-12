def leiaint(num):
    try:
        n = int(input(num))
    except:
        print('\033[91mParece que tivemos um problema. Vamos tentar novamente.\033[m')
        while True:
            n = str(input(num)).strip()
            if n.isnumeric() == True:
                n = int(n)
                if n == 0:
                    print('\033[31mvalor 0 não é um valor válido.\033[m')
                else:
                    break

            print('\033[91mParece que tivemos um problema. Vamos tentar novamente.\033[m')

    else:
        if n == 0:
            print('\033[31mvalor 0 não é um valor válido.\033[m')
            while True:
                n = str(input(num)).strip()
                if n.isnumeric() == True:
                    n = int(n)
                    break
                print('\033[91mParece que tivemos um problema. Vamos tentar novamente.\033[m')
    finally:
        return n


def leiafloat(num):
    try:
        n = float(input(num))
    except:
        print('\033[91mParece que tivemos um problema. Vamos tentar novamente.\033[m')
        while True:
            try:
                n = float(input(num))
            except:
                print('\033[91mParece que tivemos um problema. Vamos tentar novamente.\033[m')
                n = float(input(num))
                break
            if n == 0:
                print('\033[31mvalor 0 não é um valor válido.\033[m')
            else:
                break
    else:
        if n == 0:
            print('\033[31mvalor 0 não é um valor válido.\033[m')
            while True:
                n = str(input(num)).strip()
                if n.isnumeric() == True:
                    n = float(n)
                    break
                print('\033[91mParece que tivemos um problema. Vamos tentar novamente.\033[m')
    finally:
        return n


#Programa Principal:
n = leiaint('Digite um número inteiro: ')
n1 = leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n}, e o real {n1:.1f}')
div = n / n1
print(f'A divisão entre {n} e {n1} é {div}')