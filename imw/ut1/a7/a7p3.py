import sys


number1 = int(sys.argv[1])
number2 = int(sys.argv[2])

if number1 and number2 >= 1:
    if number1 < number2:
        for i in range(number1, 0, -1):
            rest = number1 % i
            if rest == 0:
                rest2 = number2 % i
                if rest2 == 0:
                    print(i)
                    break
    elif number1 == number2:
        print(number1)
    else:
        for i in range(number2, 0, -1):
            rest = number2 % i
            if rest == 0:
                rest2 = number1 & i
                if rest2 == 0:
                    print(i)
                    break

else:
    print("Error. El número no es positivo.")
