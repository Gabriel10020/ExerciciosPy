soma = 0
for c in range(1, 7):
    n = int(input('\033[96mDigite um número: '))
    if n % 2 == 0:
        soma += n
print(f'\033[94mA soma dos números pares números digitados é: {soma}')