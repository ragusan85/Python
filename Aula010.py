'''nome = str(input('Qual seu nome: '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')'''

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi: {m:.1f}')
'''if m >= 6.0:
    print('Sua média foi boa! Parabens!')
else:
    print('Sua média foi ruim! Estude mais!')'''
print('Parabens!' if m >=6 else 'Estude mais!') '''Condição Simplificada'''
