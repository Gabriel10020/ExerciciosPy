def voto(ano=0):
    from datetime import datetime
    atual = datetime.today().year
    if ano == 0:
        ano = int(input('Digite seu ano de nascimento: '))
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos, seu voto é Negado'
    elif idade >= 16 and idade <= 18 or idade >= 65:
        return f'Com {idade} anos, seu voto é Opcional'
    else:
        return f'Com {idade} anos, seu voto é Obrigatório'


#Programa Principal:
print(voto())