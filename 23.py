n = str(input('Digite um número: '))
nem = "000" + n
unidade = nem[-1]
print(f'O número da unidade é o  {unidade}')
dezena = nem[-2]
print(f'O número da dezena é o {dezena}')
centena = nem[-3]
print(f'O número da centena é {centena}')
milhar = nem[-4]
print(f'O número do milhar é {milhar}')
