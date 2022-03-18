print("Ejercicio 9 - MiniCalculadora")
print("--------------------------------")
print("Introduce un numero real: ")
x = float(input())
print("Introduce otro numero real: ")
y = float(input())
print("Introduce el signo de la operacion: ")
op = input()

if op == '+':
    suma = x+y
    print("{0:.2f} + {1:.2f} = {2:.2f}" .format(x,y,suma))
elif op == '-':
    resta = x-y
    print("{0:.2f} - {1:.2f} = {2:.2f}" .format(x,y,resta))
elif op == '*':
    mul = x*y
    print("{0:.2f} * {1:.2f} = {2:.2f}" .format(x, y, mul))
elif op == '/':
    div = x/y
    print("{0:.2f} / {1:.2f} = {2:.2f}" .format(x, y, div))
else:
    print("Operador incorrecto")