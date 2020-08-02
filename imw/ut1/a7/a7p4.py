import sys

number = int(sys.argv[1])
multi = 1
if number <= 0:
    print ("Error, el número no es positvo.")
    sys.exit()
else:
    for i in range(1, number + 1):
        multi = multi * i
        print (i, "!", multi)
