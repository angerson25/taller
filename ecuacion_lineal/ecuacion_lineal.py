#Programa: resolver una ecuación de primer grado.

import math


print("---------------------")
print("---ECUACION-LINEAL---")
print("---------------------")

#INPUT
a=int(input("Digite el valor a: "))
b=int(input("Digite el valor b: "))
c=int(input("Digite el valor c: "))



#PROCESAMIENTO
if a != 0:
        x = (c-b)/a
        print("La solucion es: " +str(x))
else:
    if  a == 0 and  b != 0:
        print("La ecuacion no tiene solucion.")
    else:
        print("La ecuacion tiene infinitas soluciones.")
print(" ")