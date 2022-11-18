#escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros.

n1 = float(input('Digite sua metragem: '))
cm = n1*100
mm = n1*1000
km = n1/1000
he = n1/100
de = n1/10
dec = n1*10
print(f'A medida de {n1}m corresponde a {cm:.2f} centimetros, {mm:.2f} milimetros, {km:.2f} quilometros, {he:.2f} hectometros,  {de:.2f} decametros, {dec:.2f} decimetros. ')
