colocados = ('Palmeiras', 'Santos', 'Vasco da Gama', 'Grêmio', 'Flamengo', 'Corinthians',
             'Internacional', 'Cruzeiro', 'São Paulo', 'Atlético Mineiro', 'Botafogo',
             'Fluminense', 'Coritiba', 'Bahia', 'Goiás', 'Guarani', 'Sport', 'Portuguesa',
             'Atlético Paranaense', 'Vitória')
print(f'Os cinco primeiros são: {colocados[:5]}')
print(f'os 4 ultimos são: {colocados[-4:]}')
alfabetico = sorted(colocados)
santos = colocados.index('Santos')
print(f'Em ordem alfabetica a lista fica: {alfabetico}')
print(f'O Santos está na posição {santos + 1}')
