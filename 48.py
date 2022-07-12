soma = 0
for c in range(3, 500, 3):
    if c % 2 == 1:
        soma += c
print(f'\033[93mA soma entre todos os números ímpares e multiplos de 3 no intervalo de 1 - 500'
      f'é igual a \033[97m{soma}')
