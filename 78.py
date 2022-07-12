valores = []
menor = maior = maiorpos = menorpos = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c} ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'Os valores digitados foram: {valores}')
print(f'O maior valor encontrado foi {maior} nas posições ', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i + 1}', end=' ')
print(f'\nO menor valor encontrado foi {menor} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i + 1},', end=' ')