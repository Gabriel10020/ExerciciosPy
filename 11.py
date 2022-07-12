altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a larguda da parede :'))
m2 = largura * altura
litros = m2 / 2
print(f'A área é de {m2} metros quadrados, para pintar essa parede'
      f'você vai precisar de {litros} litros de tinta')
