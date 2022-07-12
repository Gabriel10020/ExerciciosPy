import datetime
ano = datetime.datetime.today().year
menor = maior = 0
for c in range(1, 7):
    n = int(input('digite seu ano de nascimento: '))
    idade = ano - n
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f'Das 6 pessoas, {menor} são menores de idade e {maior} são maiores.')
