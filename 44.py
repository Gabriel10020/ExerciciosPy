produto = float(input('\033[97mDigite o preço do produto: '))
print('\033[37m=-=' * 17)
print('\033[96m[1] À vista no dinheiro ou no cheque \033[92m(10% de desconto) \n'
      '\033[96m[2] À vista no cartão \033[92m(5% de desconto)\n'
      '\033[96m[3] Em até 2 vezes no cartão \033[37m(preço formal) \n'
      '\033[96m[4] 3x ou mais no cartão \033[91m(20% de juros)')
print('\033[37m=-=' * 17)
metodo = int(input('\033[97mEscolha o método de pagamento: '))
if metodo == 1:
    desconto = produto * 10 / 100
    total = produto - desconto
    print(f'\033[34mO total do seu produto será de R${total:.2f}\n')
    print('\033[92mDesconto já incluso!\033[m')
elif metodo == 2:
    desconto = produto * 5 / 100
    total = produto - desconto
    print(f'\033[34mO total do seu produto será de R${total:.2f}\n')
    print('\033[92mDesconto já incluso!')
elif metodo == 3:
    total = produto / 2
    print(f'\033[34mVocê pagará 2 parcelas de R${total:.2f}')
elif metodo == 4:
    nvezes = int(input('Em quantas vezes deseja pagar?'))
    if nvezes < 3:
        print('\033[91mErro! Tente novamente!')
    else:
        juros = produto * 20 / 100
        total = produto + juros
        parcelas = total / nvezes
        print(f'\033[91mO total do seu produto será de R${total:.2f} com juros já inclusos!\n'
              f'{nvezes} parcelas de R${parcelas:.2f}.')
else:
    print('\033[91mOpção Inválida! Tente novamente!')
