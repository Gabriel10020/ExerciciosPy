def leiaDinheiro(num):
    numero = str(input(num)).strip()
    while True:
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            print(f'\033[31mErro! {numero} é um número inválido.\033[m')
            numero = str(input(num)).strip()
    return numero

