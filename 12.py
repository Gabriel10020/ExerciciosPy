produto = float(input('Digite o preço do produto: R$'))
desconto = produto * 5 / 100
final = produto - desconto
print(f'O preço do produto com 5% de desconto fica R${final:.2f}')