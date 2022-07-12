from random import randint
print('\033[96m-=' * 13)
print('\033[97m         Jokenpô')
print('\033[96m-=' * 13)
print('\033[34mVamos jogar!')
print('\033[97m[1] Para escolher Pedra\n'
      '[2] Para escolher Tesoura\n'
      '[3] Para escolher Papel')
jogador = int(input('\033[93mEscolha sua jogada: '))
pc = randint(1, 3)
print('\033[96m-=' * 13)
if jogador == 1:
    if jogador == 1 and pc == 1:
        print('\033[37mEu coloquei Pedra.\n\033[93mParece que deu empate!')
    elif jogador == 1 and pc == 2:
        print(f'\033[37mEu coloquei tesoura.\n\033[92mVocê venceu!')
    elif jogador == 1 and pc == 3:
        print(f'\033[37mEu coloquei Papel\n\033[31mEu venci!')
elif jogador == 2:
    if jogador == 2 and pc == 1:
        print(f'\033[37mEu coloquei Pedra.\n\033[31mVocê perdeu!')
    elif jogador == 2 and pc == 2:
        print(f'\033[37mEu coloquei tesoura.\n\033[93mParece que deu empate!')
    elif jogador == 2 and pc == 3:
        print(f'\033[37mEu coloquei Papel\n\033[91mEu perdi!')
elif jogador == 3:
    if jogador == 3 and pc == 1:
        print('\033[37mEu coloquei pedra.\n\033[31mParece que você venceu.')
    elif jogador == 3 and pc == 2:
        print(f'\033[37mEu coloquei tesoura.\n\033[91mParece que eu perdi.')
    elif jogador == 3 and pc == 3:
        print(f'\033[37mEu coloquei papel.\n\033[93mParece que deu empate!')
else:
    print(f'\033[31m{jogador} não é uma opção válida. Tente novamente!')
