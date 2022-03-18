print("Ejercicio 4 - CalificaciónFinal")
print("---------------------------------\n")
print("Introduce la nota de teoria: ")
teoria = float(input())*0.6
print("Introduce la nota de practicas: ")
practica = float(input())*0.3
print("Introduce la nota de participacion del alumno: ")
participacion = float(input())*0.1
total = float(teoria+practica+participacion)
print("La nota total es: {0:.2f}" .format(total))