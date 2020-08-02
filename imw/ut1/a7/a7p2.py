import sys

number = int(sys.argv[1])

if number <= 0:
    print ("No existe")
    sys.exit()

elif number > 0:
    sum = 0
    for i in range(1, number + 1):
        j = i ** 2
        sum = j + sum
    else:
        print (sum)
