primeiro = int(input('Digite o primeiro termo da P.A; '))
razao = int(input('Agora digite a razão da P.A: '))
count = 1
termo = primeiro
while count <= 10:
    print(f'{termo} >', end=' ')
    termo += razao
    count += 1
print('fim')