import sys

dni = int(sys.argv[1])

rest = dni % 23
text = "TRWAGMYFPDXBNJZSQVHLCKE"

print(f"{dni}{text[rest]}")
