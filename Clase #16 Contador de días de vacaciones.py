print("Hola! Este es tu contador de días de vacaciones Rappi \n")

nombre_empleado = input("Cual es tu nombre?: ")
departamento_empleado = int(input("Cual es el numero de tu departamento?: "))
antiguedad_empleado = float(input("Cuanto tiempo tienes de antiguedad?: "))

if departamento_empleado == 1:

    if antiguedad_empleado > 0 and antiguedad_empleado < 2:
        print(nombre_empleado + ", tus vacaciones correspondientes son 6 dias.")

    elif antiguedad_empleado > 2 and antiguedad_empleado < 7:
        print(nombre_empleado + ", tus vacaciones correspondientes son 14 dias.")

    elif antiguedad_empleado >= 7:
        print(nombre_empleado + ", tus vacaciones correspondientes son 20 dias.")
    
elif departamento_empleado == 2:
    if antiguedad_empleado > 0 and antiguedad_empleado < 2:
        print(nombre_empleado + ", tus vacaciones correspondientes son 7 dias.")

    elif antiguedad_empleado > 2 and antiguedad_empleado < 7:
        print(nombre_empleado + ", tus vacaciones correspondientes son 15 dias.")

    elif antiguedad_empleado >= 7:
        print(nombre_empleado + ", tus vacaciones correspondientes son 20 dias.") 

elif departamento_empleado == 3:
    if antiguedad_empleado > 0 and antiguedad_empleado < 2:
        print(nombre_empleado + ", tus vacaciones correspondientes son 10 dias.")

    elif antiguedad_empleado > 2 and antiguedad_empleado < 7:
        print(nombre_empleado + ", tus vacaciones correspondientes son 20 dias.")

    elif antiguedad_empleado >= 7:
        print(nombre_empleado + ", tus vacaciones correspondientes son 30 dias.") 

else:
    print("La clave es inexistente")
    print("Vuelve a intentarlo mas tarde")    

 
                     


      
