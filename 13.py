salario = float(input('Digite o seu salário atual: R$'))
aumento = salario * 15 / 100
total = salario + aumento
print(f'Com o reajuste de salário de 15%, o seu salário '
      f'vai ter um acrescimo de R${aumento:.2f} ficando'
      f' R${total:.2f}')