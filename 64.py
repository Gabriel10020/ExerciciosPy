n = 0
count = 0
soma = 0
while n != 999:
    n = int(input('\033[97mDigite um número [999 para parar]: '))
    count += 1
    soma += n
countfinal = count - 1
somafinal = soma - 999
print(f'\033[34m{countfinal} números foram digitados, e a soma entre eles é {somafinal}')