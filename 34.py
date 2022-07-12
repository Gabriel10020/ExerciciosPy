salario = float(input('\033[31mDigite o seu salário atual: '))
if salario >= 1250.00:
    aumento = salario * 10 / 100
    total = salario + aumento
    print(f'\033[36mSeu salário terá um aumento de 10% e ficará R${total:.2f}')
else:
    aumento = salario * 15 / 100
    total = salario + aumento
    print(f'\033[36mSeu salário terá um aumento de 15% e ficará R${total:.2f}')
