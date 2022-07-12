from math import pow , sqrt
oposto = float(input('Informe o comprimento do cateto oposto: '))
adjacente = float(input('Informe o comprimento do cateto adjacente '))
hipotenusa1 = (pow(oposto, 2)) + pow(adjacente, 2)
hipotenusa2 = sqrt(hipotenusa1)
print(f'Comprimento da hipotenusa é igual a : = {hipotenusa2:.2f}')