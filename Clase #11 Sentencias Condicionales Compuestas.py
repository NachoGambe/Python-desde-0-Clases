print("Sistema para calcular el promedio de un alumno.")

nombre = input ("Para comenzar, cual es tu nombre: ")

matematicas = float(input(nombre + " Cual es tu nota en matematicas?: "))
quimica = float(input(nombre + " Cual es tu nota en quimica?: "))
biologia = float(input(nombre + " cual es tu nota en biologia: "))

promedio = (matematicas + quimica + biologia) / 3

promedio = float(promedio)

if promedio  >= 6:
    
    print('Felicidades ' + nombre + ' "Aprobaste!" con un promedio de: ', round(promedio,2))

else:
    print("Que lástima " + nombre + " reprobaste! con un promedio de: ", round(promedio,2))

print("Fin")
