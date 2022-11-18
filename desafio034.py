'''Escreva um programa que pergunte o salário de um fiuncionario e calcule o valor do seu aumento.
Para salarios superiores a R$1.250, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento e de 15%'''

salario = float(input('Digite seu salário: '))

if salario <= 1.250:
    print(f'Voce recebeu um aumento de 10% seu salario ficará em: R${(salario * 0.10)+salario :.3f}')
else:
    print(f'Voce recebeu um aumento de 15% seu salario ficara em: R${(salario * 0.15)+salario :.3F}')