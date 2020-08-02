import sys
import math

radius = float(sys.argv[1])

print ("1. Calcular el diámetro de la circunferencia:")
print ("2. Calcular el perímetro de la circunferencia:")
print ("3. Calcular el área del círculo:")
print ("4. Salir.")

option = int(input("Escoja una opción: "))

diameter = 2 * radius
perimeter = 2 * math.pi * radius
area = math.pi * radius**2

if option == 1:
    print (diameter)

elif option == 2:
    print (perimeter)

elif option == 3:
    print (area)

elif option == 4:
    print ("Salir.")

else:
    print ("Error.")
