jogador = dict()
gols = []
jogador['Nome'] = str(input('Digite o nome do jogador: '))
jogador['Partidas'] = int(input(f'Digite quantas partidas {jogador["Nome"]} jogou: '))
total = 0
cont = 0
for c in range(0, jogador['Partidas']):
    gol = int(input(f'Quantos gols na {c + 1}º partida? '))
    gols.append(gol)
    total += gol
jogador['Gools'] = gols
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas'
      f' e fez um total de {total} gols.')
for v in jogador['Gools']:
    cont += 1
    print(f'Na {cont}º partida {jogador["Nome"]} fez {v} gols')
