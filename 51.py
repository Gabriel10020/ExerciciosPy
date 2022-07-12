primeiro = int(input('\033[97mDigite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
for c in range(primeiro, primeiro + razao * 10, razao):
    print(f'\033[96m{c}...', end=' ')
print('\n\033[92mFim.')