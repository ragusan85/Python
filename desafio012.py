# Faça um algoritmo que leia o preço de um produto e mostre seu novo preco com 5% de desconto.
n1 = float(input('Digite o preço do seu produto: '))
n2 = n1*0.05
desconto = n1-n2
print(f'O preço original do seu produto é R${n1}, o valor do desconto é de R${n1-desconto}, agora o preço com o desconto aplicado é de R${n1-(n1-desconto)}')