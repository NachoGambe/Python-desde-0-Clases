print("Conversor \n")

print("Menú de opciones \n")
print("Marque 1 para convertir de numero a palabra")
print("Marque 2 para convertir de palabra a numero")

opcion = int(input("Que opcion eliges?: "))

if opcion == 1:
    print("\n Conversor de numero a palabra \n")

    opcion_uno = int(input("Que numero deseas convertir a palabra?: "))

    if opcion_uno == 1:
        print("El numero es 'UNO'")
    elif opcion_uno == 2:
        print("El numero es 'DOS'")
    elif opcion_uno == 3:
        print("El numero es 'TRES'")
    else:
        print("Error")

elif opcion == 2:
    print("\n Conversor de palabra a numero \n")

    opcion_dos = input("Que palabra deseas convertir a numero?: ")

    if opcion_dos == "Uno":
        print("El numero es '1'")
    elif opcion_dos == "Dos":
        print("El numero es '2'")
    elif opcion_dos == "Tres":
        print("El numero es '3'")
    else:
        print("Error")


else:
    print("Error")

