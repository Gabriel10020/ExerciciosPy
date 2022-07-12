import datetime
anoatual = datetime.datetime.today().year
anonasceu = int(input('\033[97mEm que ano você nasceu? '))
idade = anoatual - anonasceu
tempo = 0
if idade < 18:
    tempo = 18 - idade
    print('\033[96m-=' * 20)
    print(f'\033[92mVocê precisará se alistar daqui {tempo} anos!')
    print('\033[96m-=' * 20)
elif idade == 18:
    print('\033[96m-=' * 17)
    print(f'\033[91mVocê já se alistou? Está na hora!')
    print('\033[96m-=' * 17)
elif idade > 18:
    tempo = idade - 18
    print('\033[96m-=' * 30)
    print(f'\033[93mVocê já se alistou? '
          f'Caso não tenha, você está {tempo} anos atrasado!')
    print('\033[96m-=' * 30)
