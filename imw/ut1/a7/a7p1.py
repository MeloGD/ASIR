import sys

number = int(sys.argv[1])

if number <= 0:
    print ("No existe.")
    sys.exit()

elif number > 0:
    for i in range(2, number):
        rest = number % i
        if rest == 0:
            print ("No es primo.")
            break
    else:
        print("Es primo.")
