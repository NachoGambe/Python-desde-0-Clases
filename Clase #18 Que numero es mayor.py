print("Que numero es mayor entre: ")

primer_numero = int(input("Primer numero: "))
segundo_numero = int(input("Segundo numero: "))
tercer_numero = int(input("Tercer numero: "))

if primer_numero > segundo_numero and primer_numero > tercer_numero:
    print("El numero ", primer_numero, " es el mayor.")

if segundo_numero > primer_numero and segundo_numero > tercer_numero:
    print("El numero ", segundo_numero, " es el mayor.")

if tercer_numero > segundo_numero and tercer_numero > primer_numero:
    print("El numero ", tercer_numero, " es el mayor.")
