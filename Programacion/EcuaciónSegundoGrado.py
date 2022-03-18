from math import *


print("Ejercicio 6 - EcuaciónSegundoGrado")
print("------------------------------------")
print("Introduce el valor de a: ")
a = float(input())
print("Introduce el valor de b: ")
b = float(input())
print("Introduce el valor de c: ")
c = float(input())
if a == 0:
    print("No se puede dividir entre 0")
else:
    x1 = float((-b+sqrt(b**2-4*a*c))/(2*a))
    x2 = float((-b-sqrt(b**2-4*a*c))/(2*a))

    print("La ecuacion es: {0:.2f} y {1:.2f}" .format(x1,x2))
