#Programa: determinar si la suma de los dos últimos dígitos de un numero es un número de 1 dígito.

import math


print("----------------------------")
print("---SUMA-ULTIMOS-2-DIGITOS---")
print("----------------------------")

#INPUT
n=input("Digite un numero: ")
n=int(n)

#PROCESAMIENTO
c1=n%10
c2= ((n%100)-c1)//10
S=c1+c2

if S<10:
    print("El resultado es de 1 digito")
else:
    print("La suma es de 2 digitos")
