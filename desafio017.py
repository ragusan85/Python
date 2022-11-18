#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triangulo, calcule e mostre o comprimento da hipotenusa
import math
catetooposto = float(input('Digite o cateto oposto: '))
catetoadjacente = float(input('Digite o cateto adjacente: '))
raizquadradacatetooposto = (catetooposto*catetooposto)
raizquadradacatetoadjacnte = (catetoadjacente*catetoadjacente)
soma = raizquadradacatetoadjacnte+raizquadradacatetooposto
raiz = math.sqrt(soma)
print(f'O comprimento da hipotenusa é: {raiz}')