from tkinter import N


n1 = int(input('Digite um valor = '))
n2 = int(input('Digite outro número = '))
s = n1 + n2
m = n1 * n2
d = n1/ n2
di = n1 // n2
e = n1 ** n2
print ('A soma é {}, \n o produto é {}, e a \n divisao é {:.3f}'.format(s,m,d), end='')
print (' Divisao inteira {} e potencia {}'.format(di,e))
#para quebra de linha \n, para nao quebrar a linha , end=''
