#Programa: determinar si cierto numero es un numero positivo de 4 digitos.

import math
s=""

print("-----------------")
print("----DETERMINAR-SI-UN-NUMERO-ES-POSITIVO-Y-DE-4-DIGITOS----")
print("-----------------")

#INPUT
n=int(input("Digite un numero: "))

#PROCESAMIENTO
d = int( n / 1000 ) 
if 1 <= d <= 9:
    s="SI"
else:
    s="NO"

#OUTPUT
print("------------------")
print("----RESULTADO----")
print("El numero " + str(n) + ", " + str(s) + " es un numero positivo de cuatro digitos.")