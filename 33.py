a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
maior = menor = 0
if a > b and c:
    maior = a
    if b > c:
        menor = c
    else:
        menor = b
if b > a and c:
    maior = b
    if a > c:
        menor = c
    else:
        menor = a
if c > a and b:
    maior = c
    if a > b:
        menor = b
    else:
        menor = a
print(f'Dos números ditos, o menor é {menor} e o maior é {maior}')