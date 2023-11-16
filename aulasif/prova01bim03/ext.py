produtos = []

while True:
    produto = input('Insira o nome do produto a seguir (parar para parar): ')
    if produto.lower() == 'parar':
        break
    produtos.append(produto)
    preco = float(input('Insira a seguir o preço do produto que acabou de digitar: '))
    produtos.append(preco)

print('O estoque atual da loja é o seguinte:\n\n')
for x in range (0, len(produtos), 2):

    print(f'Produto: {produtos[x]}\nPreço em R$ {produtos[x+1]}\n\n')