'''Faça um programa que leia o nome compoleto de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
EX: Ana Maria de Souza
Primeiro: Ana
Ultimo: Souza'''
nome = str(input('Digite seu nome completo: ')).split()
cont = len(nome)
primeiro = nome[0]
segundo = nome[cont-1]
print(f'Seu primeiro nome é: {primeiro} seu segundo nome é: {segundo}')
