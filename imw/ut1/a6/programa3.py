import sys


media = float(sys.argv[1])

if media < 5:
    print ("Suspenso.")

elif 5 <= media < 7:
    print ("Aprobado.")

elif 7 <= media < 9:
    print ("Notable.")

elif 9 <= media < 10:
    print ("Sobresaliente.")

elif media == 10:
    print ("Matricula de honor.")

else:
    print ("Error.")
