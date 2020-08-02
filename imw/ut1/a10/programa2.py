import sys

def add_contacts(phone_book, name, phone):
    phone_book[name] = phone
def show_contacts(phone_book):
    print("\n")
    if phone_book == {}:
        print("Lista vacía.")
    for name, number in phone_book.items():
        print("{}: {}".format(name, number))
    print("\n")
    input("Pulsa una tecla para volver.")
def remove_contacts(phone_book, name):
    del(phone_book[name])
def menu():
    phone_book = {}
    while True:
        print("1. Mostrar contactos")
        print("2. Añadir contactos")
        print("3. Eliminar contactos")
        print("4. Salir")
        option = input("Selecciona una opción:")
        option = int(option)
        if option == 1:
            show_contacts(phone_book)
        if option == 2:
            name = input("¿Cuál es el nombre?")
            if name in phone_book:
                print("Ya existe")
            else:
                phone = input("¿Cuál es el número?")
                add_contacts(phone_book, name, phone)
        if option == 3:
            name = input("¿A quién quieres eliminar?")
            if name in phone_book:
                remove_contacts(phone_book, name)
            else:
                print("Nombre incorrecto.")
        if option == 4:
            sys.exit("Adios")
menu()
