nome = str(input('Digite o seu nome: '))
nuome = nome.split()
espaco = nome.count(' ')
print(f'Seu nome completo é {nome.upper()}')
print(f'Em minúsculo fica {nome.lower()}')
print(f'Seu nome tem {len(nome) - espaco} letras')
print(f'Seu primeiro nome é {nuome[1]} e ele tem {len(nuome[0])} Letras')
