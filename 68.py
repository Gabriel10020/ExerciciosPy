from random import randint
print('\033[97mVamos jogar par ou impar!')
count = p = soma = 0
while True:
    pc = randint(1, 10)
    p = str(input('\033[97mEscolha par ou impar: [P/I]')).upper().strip()[0]
    if p == 'I':
        pcpar = 'P'
    else:
        pcpar = 'I'
    n = int(input('\033[94mEscolha seu número agora: '))
    soma = pc + n
    if soma % 2 == 0:
        if pcpar == 'I':
            print(f'\033[92mEu coloquei {pc}, parece que você venceu! vamos de novo!')
            count += 1
        elif pcpar == 'P':
            print(f'\033[91mEu coloquei {pc}, deu par e eu venci!')
            break
    elif soma % 2 == 1:
        if pcpar == 'P':
            print(f'\033[92mEu coloquei {pc}, parece que você venceu! vamos de novo!')
            count += 1
        elif pcpar == 'I':
            print(f'\033[91mEu coloquei {pc}, deu impar e eu venci!')
            break
print('\033[97m-=' * 20)
print(f'Você venceu um total de {count} vitórias consecutivas')

