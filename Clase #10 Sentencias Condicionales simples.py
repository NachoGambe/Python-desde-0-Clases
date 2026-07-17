print("Sistema para calcular el promedio de un alumno.")

nombre = input ("Para comenzar, cual es tu nombre: ")

matematicas = int(input(nombre + " Cual es tu nota en matematicas?: "))
quimica = int(input(nombre + " Cual es tu nota en quimica?: "))
biologia = int(input(nombre + " cual es tu nota en biologia: "))

promedio = (matematicas + quimica + biologia) / 3

promedio = float(promedio)

if promedio  >= 6:
    print('Felicidades ' + nombre + ' "Aprobaste!" con un promedio de: ', promedio)

print("Fin")
