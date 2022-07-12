def ficha(nome='', n=0):
    nome = str(input('Digite o nome do jogador: ')).strip().capitalize()
    if nome == '':
        nome = 'Desconhecido'
    n = str(input('Digite quantos gols foram feitos pelo jogador: ')).strip()
    if n == '':
        n = 0
    if n.isnumeric() == False:
        n = 0

    print(f'O jogador {nome} fez {n} gol(s) no campeonato.')


#Programa Principal:
ficha()
