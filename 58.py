from random import randint
pc = randint(0, 10)
print('\033[97mVamos jogar um jogo!\n'
      'Vou pensar em um número entre 0 e 10, tente adivinhar!')
jogador = int(input('\033[93mQual número você acha que é? '))
while jogador != pc:
    print('\033[91mVocê errou!', end=' ')
    jogador = int(input('Tente novamente: '))
print(f'\033[92mParabéns! você acertou! eu penseno no número {pc}')