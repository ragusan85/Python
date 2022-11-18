'''Faça um programa que leia um número de 0 a 999 e mostre na tela cada um dos digitos separados
EX: Digite um número: 1834

Unidade 4
dezena 3
centena 8
milhar 1'''

numero = int(input('Digite um numero com 4 digitos: '))
divi = numero.split()
primeiro = divi[0]
segundo = divi[1]
terceiro = divi[2]
quarto = divi[3]



print(f'As unidades sao: {primeiro} as dezenas sao: {segundo} as centenas são {terceiro} e os milhares são {quarto}')