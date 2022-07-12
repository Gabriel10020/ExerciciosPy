n = int(input('Digite um número: '))
maior = menor = n
continuar = ''
count = 1
soma = 0
while continuar != 'N':
    continuar = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
    if continuar == 'S':
        n = int(input('Digite outro número: '))
        count += 1
        soma += n
        if n > maior:
            maior = n
        elif menor > n:
            menor = n
media = soma / count
print(f'{count} números foram digitados. a média entre eles é {media}\n'
      f'desses números, o menor é {menor}, e o maior é {maior}')