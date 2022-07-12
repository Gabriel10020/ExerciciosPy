distancia = int(input('De quantos Km será a viagem? '))
if distancia > 200:
    kmtragem = 0.45
    custo = distancia * kmtragem
    print(f'Sua passagem irá custar R${custo:.2f}.')
    print('Cada km está saindo a R$0,45.')
else:
    kmtragem = 0.50
    custo = distancia * kmtragem
    print(f'Sua passagem irá custar R${custo:.2f}.')
    print('Cada km está saindo a R$0,50.')
