import sys
import math

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])
x3 = float(sys.argv[5])
y3 = float(sys.argv[6])

d1 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
d2 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)

if d2 > d1:
    print(
        "El punto más cercano a (", x1, ",", y1,
        ") es (", x2, ",", y2, ") y está a una distancia de ",
        d1
    )
else:
    print(
        "El punto más cercano a (", x1, ",", y1,
        ") es (", x3, ",", y3, ") y está a una distancia de ",
        d2
    )
