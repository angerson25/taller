#Programa: hallar las raices de una ecuacion de segundo grado.

import math
from math import sqrt
s=""

print("--------------------------------------")
print("---ECUACION-DE-LA-FORMA:ax² + bx + c = 0---")
print("--------------------------------------")

#INPUT

a= int(input("Ingrese el valor de a: "))
b= int(input("Ingrese el valor de b: "))
c= int(input("Ingrese el valor de c: "))

#PROCESAMIENTO

discriminante = b * b - 4 * a * c
if discriminante < 0:
    print("La ecuacion no tiene solucion en los reales")

raiz = sqrt(discriminante)

x1 =(b + raiz) / (2 * a)

x2 =(b - raiz) / (2 * a)

#OUTPUT
print("---------RESULTADOS---------")
print("La primer raiz es: "+  str(x1))
print("La segunda raiz es: "+  str(x2))