def leiaint(num):
    numero = str(input(num)).strip()
    while True:
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
            numero = str(input(num)).strip()
    return numero


#Programa Principal:
n = leiaint('Digite um número: ')
print(f'O número digitado foi o número {n}')
