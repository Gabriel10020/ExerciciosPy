n = int(input('\033[93mDigite um número inteiro para a conversão: '))
print('\033[94m-=' * 24)
print('\033[96m[1] Digite 1 para converter para binário. \n'
      '\033[96m[2] Digite 2 para converter para octal. \n'
      '\033[96m[3] Digite 3 para converter para hexadecial')
print('\033[94m-=' * 24)
bina = bin(n)
octa = oct(n)
hexa = hex(n)
escolha = int(input('\033[93mDigite aqui: '))
print('\033[94m-=' * 24)
if escolha == 1:
    print(f'\033[92mO número {n} convertido para binário é: {bina[2:]}')
elif escolha == 2:
    print(f'\033[92mO número {n} convertido para octal é: {octa[2:]}')
elif escolha == 3:
    print(f'\033[92mO número {n} convertido para hexadecial é {hexa[2:]}')
else:
    print('\033[31mOpção inválida, tente novamente!')

