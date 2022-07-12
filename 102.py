def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O valor do numero a ser faturado. (nenhum numero informado = 1)
    :param show: (Opcional) Mostrar ou não a conta
    :return: vai ser retornado o valor final do calculo do fatorial.
    """
    f = 1
    if show == True:
        print(f'{n} ', end='')
        for c in range(n - 1, 0, -1):
            f *= c
            print(f'x {c} ', end='')
        print(f' = {f}')
    else:
        for c in range(n, 0, -1):
            f *= c
        print(f)
    return f


#Programa Principal:
n = int(input('Digite um número para o fatorial: '))
fatorial(n, True)
