def dobro(n, formatado=True):
    dob = n * 2
    if formatado == True:
        return f'R${dob:.2f}'
    else:
        return dob


def metade(n, formatado=True):
    met = n / 2
    if formatado == True:
        return f'R${met:.2f}'
    else:
        return met


def aumentar(n, porcentagem, formatado=True):
    desconto = n * porcentagem / 100
    total = n + desconto
    if formatado == True:
        return f'R${total:.2f}'
    else:
        return total


def diminuir(n, porcentagem, formatado=True):
    desconto = n * porcentagem / 100
    total = n - desconto
    if formatado == True:
        return f'R${total:.2f}'
    else:
        return total


def moeda(n=0, moda='R$'):
    return f'{moda}{n:.2f}'.replace('.', ',')


def resumo(n, aum, desc):
    print('-' * 35)
    print('         RESUMO DO VALOR')
    print('-' * 35)
    print(f'Preço analisado: {moeda(n):>14}')
    print(f'Dobro Do preço: {dobro(n, True):>16}')
    print(f'Metade do preço: {metade(n, True):>14}')
    print(f'{aum}% de aumento: {aumentar(n, aum, True):>15}')
    print(f'{desc}% de redução: {diminuir(n, desc, True):>15}')
