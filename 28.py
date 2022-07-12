from random import randint
print('Vamos jogar um jogo!\n'
      'Vou pensar em um número entre 0 e 5, tente adivinhar!')
pc = randint(0, 5)
jogador = int(input('Qual número você acha que é? '))
if jogador == pc:
    print(f'Parabéns, você acerteu! eu pensei no número {pc}')
else:
    print(f'Opa! parece que você errou! '
          f'Eu pensei no número {pc}')
