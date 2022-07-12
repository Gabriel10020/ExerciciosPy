n1 = int(input('\033[96mDigite um valor: '))
n2 = int(input('Digite outro valor: '))
print('\033[97m-=' * 13)
if n1 > n2:
    print(f'\033[95mO primeiro valor é maior.\n{n1} é maior que {n2}')
elif n2 > n1:
    print(f'\033[92mO segundo valor é maior\n{n2} é maior que {n1}')
elif n1 == n2:
    print('\033[97mAmbos os valores são iguais.')
print('\033[97m-=' * 13)