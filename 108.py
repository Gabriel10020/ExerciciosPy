from UtilidadesCeV import moedas
p = float(input('Digite o preço R$: '))
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}')
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}')
print(f'Aumentando 10% fica {moedas.aumentar(p, 10, True)}')
