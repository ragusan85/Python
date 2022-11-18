'''Escreva um programa que faça o computador ''pensar'' em um numero inteiro entre 0 e 5 e peça poara o usuário tentar descobrir qual foi
 o número escolhido pelo computador
 o Programa deverá escrever na tela se o usuário venceu ou perdeu'''

import random
n = random.randrange(5)
gente = int(input('Digite um número entre 1 e 5: '))
if n == gente:
    print('Acertou miserávi!')
else:
    print('errou')
          