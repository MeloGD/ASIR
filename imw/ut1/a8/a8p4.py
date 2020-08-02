import sys

number = list(sys.argv)
##Si no hacemos el del, también metera en la lista el nombre del programa a8p4.py
del number[0]
numbers = len(number)
count = 0

for i in number:
    i = float(i)
    count = count + i
total = count / numbers
print("La media es:{}".format(total))
