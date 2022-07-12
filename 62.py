primeiro = int(input('Digite o primeiro termo da P.A; '))
razao = int(input('Agora digite a razão da P.A: '))
count = 0
termo = primeiro
while count <= 10:
    termo += razao
    count += 1
    print(f'{termo} >', end=' ')
print('pausa')
mais = int(input('\nQuantos mais termos quer mostrar? '))
while mais != 0:
    count = 0
    termo += razao
    while count < mais:
        print(f'{termo} >', end=' ')
        termo += razao
        count += 1
    print('pausa')
    mais = int(input('\nQuantos mais termos quer mostrar? '))
print('Fim')