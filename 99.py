def contador(* num):
    print('-=' * 23)
    maxs = max(num)
    print(f'Os valores analizados foram: ', end=' ')
    for c in num:
        print(c, end=' ')
    print('')
    print(f'Dos {len(num)} Valores inseridos, o maior foi o {maxs}')


#Começo Do Programa:
contador(1, 5, 6, 2, 8, 4, 3)
contador(9, 2, 0, 3, 5, 11, 2)
contador(8, 2, 4, 1, 3)
contador(2, 3, 5, 2)
