'''Escreva um programa que leia a velocidade de um carro
Se ele pasar de 80 KM/H, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada KM acima do limite
'''

velocidade = int(input('Digite a sua velocidade: '))
taxa = velocidade-80
if velocidade >= 80:
    print (f'Voce foi multado, a sua multa vai custar R${taxa*7}')
else:
    print('Voce nao foi multado.')