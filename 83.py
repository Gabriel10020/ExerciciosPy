exp = str(input('Digite a expressão: ')).strip()
aberto = fechado = 0
for c in exp:
    if c == '(':
        aberto += 1
    elif c == ')':
        fechado += 1
if aberto == fechado:
    print('Sua expressão é válida.')
else:
    print('Sua expressão é inválida.')
