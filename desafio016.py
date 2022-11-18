#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: digite 6.656 mostre somente 6

import math
num = float(input('Digite um número real: '))
print(f'Seu número inteiro é {math.floor(num)}')


