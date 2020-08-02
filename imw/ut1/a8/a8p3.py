import sys

k = int(sys.argv[1])
string = sys.argv[2]

if k < 0:
    print("No es positivo.")
    sys.exit("Expulsado.")

else:
    string_list = string.split(" ")
    count = 0
    for word in string_list:
        if len(word) == k:
            count += 1

    print(f"Hay {count} palabras de tamaño {k}.")
