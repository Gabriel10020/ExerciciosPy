from  UtilidadesCeV import moedas
num = int(input('Digite um número:  '))
porc = int(input('Agora digite uma porcentagem: '))
print(f'O dobro desse número é {moedas.dobro(num)}\n'
      f'A metade é {moedas.metade(num)}\n'
      f'{num} menos {porc}% é {moedas.diminuir(num, porc)}\n'
      f'{num} mais {porc}% é {moedas.aumentar(num, porc)}')

