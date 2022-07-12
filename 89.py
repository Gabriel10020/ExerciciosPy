turma = list()
aluno = list()
pos = 0
while True:
    aluno.clear()
    aluno.append(str(input('Digite o nome do aluno: ')))
    aluno.append(float(input('Digite a primeira nota: ')))
    aluno.append(float(input('Digite a segunda nota: ')))
    turma.append(aluno[:])
    print('---' * 15)
    continuar = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    while True:
        if continuar in 'SN':
            break
        print('Opção inválida, tente novamente!')
        continuar = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print('-=' * 22)
print('             Média Da Turma     ')
print('-=' * 22)
print(f'{"Nº":<4}{"nome":^17}{"Media":>16}')
print('---' * 15)
for c in turma:
    media = (c[1] + c[2]) / 2
    print(f'Nº{pos:<4}{c[0]:^15}{media:>14.1f}')
    pos += 1
while True:
    n = int(input('Deseja ver as notas de qual aluno? [999 para parar]'))
    if n == 999:
        break
    elif n > len(turma):
        while n > len(turma):
            n = int(input('Número inválido. tente novamente: '))
    print(f'As notas de {turma[n][0]} são: {turma[n][1]} e {turma[n][2]}')
    print('---' * 15)
print('Fim')
