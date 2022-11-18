'''Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario de elsas podem ou nao formar um triangulo.'''
r1 = int(input('Digite o tamanho da Linha A: '))
r2 = int(input('Digite o tamanha da Linha B: '))
r3 = int(input('Digite o tamanho da Linha C: '))
if r1 < (r2 + r3):
    print('Seu com essas medidas é possivel fazer um triangulo!')
else:
    print('Com essas medidas nao é possivel fazer um triangulo.')
