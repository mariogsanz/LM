from math import sqrt


print("Ejercicio 7 - Hipotenusa")
print("--------------------------")
print("Introduce el tamaño del cateto: ")
cat1 = float(input())
print("Introduce el tamaño del otro cateto: ")
cat2 = float(input())
a = sqrt(cat1**2 + cat2**2)
print("La hipotenusa es {0:.2f}" .format(a))