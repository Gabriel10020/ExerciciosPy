n = int(input('Digite uma distância em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print(f'A distância é de {n} metros.\n'
      f'Em quilometros são {km} km\n'
      f'Em hectometros são {hm} hm\n'
      f'Em Decametros são {dam} dam\n'
      f'Em decimetros são {dm} dm\n'
      f'Em centimetros são {cm} cm\n'
      f'Em milimetros são {mm} mm')

