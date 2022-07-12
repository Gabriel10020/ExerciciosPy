aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['Media'] = float(input('Digite sua média: '))
if aluno['Media'] < 5:
    aluno['Situação'] = 'Reprovado'
elif aluno['Media'] >= 5 and aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
elif aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
print('-=' * 25)
for k, v in aluno.items():
    print(f'   ---- O {k} é {v}')