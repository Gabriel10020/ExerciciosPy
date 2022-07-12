peso = float(input('\033[97mDigite o seu peso em Kg: '))
altura = float(input('Digite a sua altura atual: '))
imc = peso / (altura * altura)
print('\033[37mx=' * 20)
if imc < 18.5:
    print(f'\033[36mSeu IMC é de {imc:.1f}. Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print(f'\033[92mSeu IMC é de {imc:.1f}. Você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print(f'\033[93mSeu IMC é de {imc:.1f}. Você está acima do peso!')
elif imc >= 30 and imc < 40:
    print(f'\033[33mSeu IMC é de {imc:.1f} Você está obeso!')
elif imc > 40:
    print(f'\033[31mSeu IMC é de {imc:.1f}. Você está na obesidade morbida!\n'
          f'Você precisa se cuidar urgentemente!')
print('\033[37mx=' * 20)