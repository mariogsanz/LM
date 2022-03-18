print("Ejercicio 14 - ParidadDivisible")
print("---------------------------------")
num1 = int(input("Introduce un numero entero: "))
num2 = int(input("Introduce otro numero entero: "))
num3 = int(input("Introduce otro numero entero: "))
paridad = num1%2

if paridad == 0:
    print("{0:d} es par" .format(num1))
else:
    print("{0:d} es impar" .format(num1))

