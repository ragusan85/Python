'''Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome SANTO'''

cidade = str(input('Digite o nome da cidade: ')).split()
d = cidade[0]
c = 'Santo' in cidade
print(c)
