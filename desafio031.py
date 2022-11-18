'''Desenvolva um programna que pergunte a distancia de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0.50 por km para viagens até 200KM e R$0.45 para viagens ais longas'''
viagem = int(input('Digite a distancia da sua viagem: '))
if viagem <= 200:
    print(f' Sua viagem foi Curta! E custará: R${viagem*0.50}')
else:
    print(f'Sua viagem foi Longa! E custará: R${viagem*0.45}')
    