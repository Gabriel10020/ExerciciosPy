import datetime
anoatual = datetime.datetime.today().year
nascimento = int(input('\033[32mEm que ano você nasceu? '))
idade = anoatual - nascimento
print('\033[97m==' * 20)
if idade < 9:
    print('\033[92mVocê será alocado na categoria Mirim!')
elif idade > 9 and idade < 14:
    print('\033[93mVocê será alocado na categoria infantil!')
elif idade >= 14 and idade < 19:
    print('\033[33mVocê será alocado na categoria Junior!')
elif idade >= 19 and idade < 25:
    print('\033[34mVocê será alocado na categoria Senior!')
elif idade >= 25:
    print('\033[96mVocê será alocado na categoria Master!')
print('\033[97m==' * 20)