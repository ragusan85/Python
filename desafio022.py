'''crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiusculas ------
o come com todas minusculas-------
Quantas letras ao todo(sem considera espaços.)--------
Quantas letras tem o primeiro nome'''


nome = input('Digite o seu nome completo: ')
mai = (nome.upper())
min = (nome.lower())
semesp = len(nome.replace(' ',''))
carprinome = nome.split()
contar1 = carprinome[0]

print(f'Seu nome com completo é: {nome}')
print(f'Seu nome com letras maisusculas é: {mai} ')
print(f'Seu nome com letras minusculas é: {min}')
print(f'Seu nome completo tem {semesp} caracteres')
print(f'Seu primeiro nome tem {len(contar1)} caracteres')
