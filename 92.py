from datetime import datetime
atual = datetime.now().year
usuario = dict()
usuario['Nome'] = str(input('Informe seu nome: '))
nasc = int(input('seu ano de nascimento: '))
usuario['Idade'] = atual - nasc
usuario['CT'] = int(input('Digite sua carteira de trabalho: (se não tiver digite 0): '))
if usuario['CT'] == 0:
    for k, v in usuario.items():
        print(f'{k} --- > {v}')
else:
    usuario['AnoC'] = int(input('Digite o ano de contratação: '))
    usuario['Salario'] = int(input('Digite seu salário: '))
