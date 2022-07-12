dias = int(input('Por quantos dias o Carro foi Alugado? '))
km = int(input('Quantos Km foram rodados com o carro? '))
n1 = dias * 60
n2 = km * 0.15
valorpago = n1 + n2
print(f'O valor a ser pago será de R${valorpago}')
print(f'R$60 cada dia e R$0,15 cada Km rodado.')