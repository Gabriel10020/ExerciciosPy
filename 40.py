n1 = float(input('\033[97mDigite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
n3 = float(input('Digite a sua terceira nota: '))
n4 = float(input('Digite a sua quarta nota: '))
media = (n1 + n2 + n3 + n4) / 4
if media < 5:
    print(f'\033[31mSua média é {media:.1f}!\nVocê está reprovado!')
elif media < 7 and media >= 5:
    print(f'\033[93mSua média é de {media:.1f}!.'
          f'Você está de recuperação!')
else:
    print(f'\033[96mParabéns! Você tirou {media:.1f} \n'
          f'Você foi Aprovado!')
