dados = []
cadastrados = ()
pessoa = {}
mulheres = []
totpessoa = totidade = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Digite o seu nome: '))
    pessoa['Idade'] = int(input('Digite sua idade: '))
    pessoa['Sexo'] = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    totpessoa += 1
    totidade += pessoa['Idade']
    dados.append(pessoa.copy())
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'])
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while True:
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
mediaidade = totidade / totpessoa
print('-=' * 30)
print(f'Todas as mulheres cadastradas foram: \n{mulheres}')
print(f'A média das idades foram: {mediaidade}')
for c, v in enumerate(dados):
    if v['Idade'] > mediaidade:
        print(f'{v["Nome"]} Está Acima da média de idade.')






