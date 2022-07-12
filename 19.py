import random
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro Aluno: '))
aluno4 = str(input('Digite o nomed o quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(lista)
print(f'O aluno sorteado foi: {sorteado}')
