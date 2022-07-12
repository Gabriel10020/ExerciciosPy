cidade = str(input('Diga o nome de uma cidade: ')).capitalize().split()
sant = 'Santo' in cidade[0]
print(f'A cidade {cidade} começa com Santo? {sant}')
