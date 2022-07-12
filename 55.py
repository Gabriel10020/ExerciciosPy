maior = float(input('Digite seu peso aqui: '))
menor = maior
for c in range(1, 6):
    n = float(input('Digite o peso aqui: '))
    if n > maior:
        maior = n
    elif menor > n:
        menor = n
print(f'O maior peso foi {maior} e o menor {menor}')