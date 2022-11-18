#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e quantidade de tinta necessária para pintalá, sabendo que cada litro de tinta pinta uma area de 2m quadrados
# quadrados

n1 = float(input('Digite a Largura da sua parede: '))
n2 = float(input('Digite a Altura da dua parede: '))
area = (n1*n2)
print ('Sua área é de',area,'Metros quadrados')
print ('Para pintar sua parede voce vai precisar de',area/2,'litros de tinta')