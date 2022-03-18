print("Ejercicio 3 - Operaciones Matemáticas")
print("---------------------------------------\n")
print("Introduce un numero: ")
num1 = float(input())
print("Introduce otro numero: ")
num2 = float(input())
suma = num1 + num2
resta = num1 - num2
mul = num1 * num2
if num2 == 0.0:
    print("Division entre 0")
else:
    div = num1 / num2

print("Suma: {0:.2f}\nResta: {1:.2f}\nMultiplicacion: {2:.2f}\nDivision: {3:.2f}" .format(suma,resta,mul,div))