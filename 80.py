lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
    elif n > lista[len(lista)-1]:
        lista.append(n)
    for p, v in enumerate(lista):
        if n > len(lista):
            lista.insert(p, n)
print(lista)

