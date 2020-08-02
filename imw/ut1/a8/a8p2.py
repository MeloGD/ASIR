import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = "".join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])

su_a = 0
su_t = 0
su_g = 0
su_c = 0

for char in sequence:
    if char == "A":
        su_a = su_a + 1
    elif char == "T":
        su_t = su_t + 1
    elif char == "G":
        su_g = su_g + 1
    elif char == "C":
        su_c = su_c + 1
print(f"Adenine:{su_a}\nThymine:{su_t}\nGuanine:{su_g}\nCytosine:{su_c}")
