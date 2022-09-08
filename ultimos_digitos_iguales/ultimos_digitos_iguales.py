#Programa: determine si los dos últimos dígitos de un numero son iguales.

import math


print("---------------------------------")
print("---ULTIMOS-DOS-DIGITOS-IGUALES---")
print("---------------------------------")

#INPUT
n=input("Digite un numero entero  : ")
n=int(n)

#PROCESAMIENTO
c1=n%10
c2= ((n%100)-c1)//10

if c1==c2:
    print("Sus dos últimos dígitos son iguales")
else:
    print("Sus dos últimos dígitos NO son iguales")



