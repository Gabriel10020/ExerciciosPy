def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Indique uma ou várias notas dos alunos(aceita várias)
    :param sit: (Opcional) sit=True para indicar a situação.
    :return: Dicionário com várias informações sobre a situação da turma
    """
    turma = dict()
    media = sum(n) / len(n)
    turma['Total'] = len(n)
    turma['Maior'] = max(n)
    turma['Menor'] = min(n)
    turma['Media'] = sum(n) / len(n)
    if sit == True:
        if media >= 7:
            turma['Situação'] = 'Ótima'
        elif media >= 5 and media < 7:
            turma['Situação'] = 'Ok'
        else:
            turma['Situação'] = 'Ruim'
    return turma


# Programa Principal:
resposta = notas(1, 2, 4, 6, 7, sit=True)
print(resposta)
help(notas)
