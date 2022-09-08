#Programa: determinar si el ultimo digito de un numero entero es par.

import math
s=""

print("-----------------")
print("----DETERMINAR-SI-EL-ULTIMO-DIGITO-DE-UN-NUMERO-ES-PAR----")
print("-----------------")

#INPUT
n=int(input("Digite un numero: "))

#PROCESAMIENTO
d= int(n % 10)
u= int(d % 2)
if u == 0:
    s="SI"
else:
    s="NO"

    
#OUTPUT
print("------------------")
print("----RESULTADOS----")
print("El ultimo digito del numero " + str(n) + " es: " + str(d) + " y, este, " + str(s) + " es par.")
