'''Faça um programa que leia uma frase pelo teclado e mostre: '''
'''Quantas vezes a palavra A'''
''' em que posição ela aparece a pprimeira vez'''
'''Em que posição ela aparece na ultima vez'''
c = str(input('Digite a sua frase: '))
mai = c.upper().count('A')
print(mai)