print("Ejercicio 10 - coincideNumerosAnteriores")
print("------------------------------------------")
num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))
num3 = int(input("Introduce un numero: "))
num4 = int(input("Introduce un numero: "))

if num4 == num1 or num4 == num2 or num4 == num3:
    print("Coincide algun numero")
else:
    print("No coindice con ninguno")