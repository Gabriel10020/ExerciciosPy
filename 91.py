from random import randint
from operator import itemgetter
lista = dict()
lista['Jogador1'] = randint(1, 6)
lista['Jogador2'] = randint(1, 6)
lista['Jogador3'] = randint(1, 6)
lista['Jogador4'] = randint(1, 6)
ordem = dict()
for k, v in lista.items():
    print(f'O {k} tirou {v} no dado.')
ordem = sorted(lista.items(), key=itemgetter(1), reverse= True)
print('-=' * 20)
c = 0
for k, v in ordem:
    c += 1
    print(f'Em {c}º ficou o {k} com {v} no dado')



