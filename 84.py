pessoa = list()
grupo = list()
pesadas = list()
leves = list()
totpessoas = 0
pessoa.append(str(input('Digite seu nome: ')).strip())
pessoa.append(float(input('Digite seu peso: ')))
grupo.append(pessoa[:])
pessoa.clear()
while True:
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while True:
        if continuar in 'SN':
            break
        print('Opção inválida, tente novamente!')
        continuar = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
    pessoa.append(str(input('Digite seu nome: ')).strip().capitalize())
    pessoa.append(float(input('Digite seu peso: ')))
    grupo.append(pessoa[:])
    pessoa.clear()
totpessoas = len(grupo)
print(f'{totpessoas} foram cadastradas.')
for p in grupo:
    if p[1] >= 100:
        pesadas.append(p[0])
    elif p[1] <= 70:
        leves.append(p[0])
print(f'A lista das pessoas mais pesadas é: {pesadas}')
print(f'A lista das pessoas mais leves é: {leves}')
