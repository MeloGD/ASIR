import sys
dinero = int(sys.argv[1])

print ("Para ", dinero, " €", "es necesario:")

dinero_50 = dinero % 50
dinero_50x = dinero // 50

if dinero_50x >= 1:
    print (dinero_50x, "billente/s de 50€.")
else:
    print ("Ninguno de 50€.")
    
dinero_20 = dinero_50 % 20 
dinero_20x = dinero_50 // 20

if dinero_20x >=1:
    print (dinero_20x, "billete/s de 20€.")
else:
    print ("Ninguno de 20€.")
    
dinero_10 = dinero_20 % 10
dinero_10x = dinero_20 // 10

if dinero_10x >= 1:
    print (dinero_10x, "billete/s de 10€.")
else:
    print ("Ninguno de 10€.")
    
dinero_5 = dinero_10 % 5
dinero_5x = dinero_10 // 5

if dinero_5x >= 1:
    print (dinero_5x," billete/s de 5€.")
else:
    print ("Ninguno de 5€.")
    
dinero_2 = dinero_5 % 2
dinero_2x = dinero_5 // 2

if dinero_2x >= 1:
    print (dinero_2x, "moneda/s de 2€.")
else:
    print ("Ninguna de 2€")
    
dinero_1 = dinero_2 % 1
dinero_1x = dinero_2 // 1

if dinero_1x >= 1:
    print (dinero_1x, "moneda/s de 1€.")
else:
    print ("Ninguna de 1€.")

