#Programa: valor de una llamada.

import math
v=""
p=int(3)

print("-----------------")
print("----VALOR-LLAMADA----")
print("-----------------")

#INPUT
d=int(input("Digite la duracion de la llamada: "))

#PROCESAMIENTO
if d <= p:
    v=300
else:
    v= (d-3) * 50 + 300

#OUTPUT
print("------------------")
print("----RESULTADOS----")
print("La llamada de " + str(d) + " minutos tiene un valor de: " + str(v) + " COP ")