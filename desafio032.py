'''Faça um programa que leia o ano e iddentifique se ele é um ano bissexto'''
ano = int(input('Digite o ano: '))
if ano % 4 == 0:
    print('Esse ano é Bissexto!')
else:
    print('Esse ano é nao é bissexto')