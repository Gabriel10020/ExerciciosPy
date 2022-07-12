casavalor = float(input('\033[36mDigite o valor da casa que quer comprar: R$ '))
salario = float(input('\033[36mPor favor digite agora o seu salário atual: R$ '))
anos = int(input('\033[36mAgora digite em quantos anos pretende pagar: '))
meses = anos * 12
mensalidade = casavalor / meses
print('\033[97m_' * 52)
if mensalidade > (salario * 30) / 100:
    print('\033[31mO valor das prestações excede 30% do seu salário!\n'
          'Infelizmente seu financiamento foi negado!')
else:
    print('\033[32mO valor das prestações não excede 30% do seu salário!\n'
          'Seu financiamento foi aprovado!')
print('\033[97m_' * 52)
