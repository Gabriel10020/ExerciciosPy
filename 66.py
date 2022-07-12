soma = count = 0
while True:
    n = int(input('Digite um número[999] para parar: '))
    if n == 999:
        break
    else:
        soma += n
        count += 1
print(f'{count} números foram digitados, e a soma entre eles é igual a {soma}')