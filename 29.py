velocidade = int(input('Diga a velocidade do carro: '))
if velocidade > 80:
    excedente = velocidade - 80
    multa = excedente * 7
    print('Você ultrapassoul o limite e será multado!')
    print(f'O preço da multa será de R${multa},00 ')
else:
    print('Muito bem, você não ultrapassou o limite'
          'de velocidade de 80Km/h e por isso não será multado!')