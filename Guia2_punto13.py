# GUIA 2 - PUNTO 13
# Desarrollar un programa que permita procesar los datos del último censo de una pequeña población.
# Por cada habitante se ingresa:sexo(M/F)y edad. La carga de datos analiza al ingresar cualquier 
# otro valor para sexo. El programa debe informar: 
# - A qué sexo corresponde la mayor cantidad de habitantes (considerar que puede ser igual)
# - Cantidad de mujeres en edad escolar (4 a 18 años inclusive)
# - Si hay algún varón que supere los 80 años de edad.

sexo = ""
N = 0
masculino = 0
femenino = 0
escolar_mujer = 0
mayor_hombre = 0

print ("Bienvenido al Censo")
N = int(input("Ingrese la cantidad de habitantes: "))

for i in range(N):
    sexo = input("Ingrese -M- para Masculino o -F- para Femenino: ").upper()

    while sexo != "M" and sexo != "F":
        print("Error. Ingrese un valor valido.")
        sexo = input("Ingrese -M- para Masculino o -F- para Femenino: ").upper()

    edad = int(input("Ingrese la edad: "))

    while edad<=0 or edad>100:
        print("Error. Ingrese una edad valida.")
        edad = int(input("Ingrese la edad: "))

    if sexo == "M":
        masculino = masculino + 1
        if edad > 80:
            mayor_hombre = mayor_hombre + 1
    else:
        femenino = femenino + 1
        if 4<=edad<=18:
            escolar_mujer = escolar_mujer + 1

print()

if masculino == femenino:
    print("La cantidad de habitantes del sexo femenino y masculino son iguales.")
elif masculino > femenino:
    print("La mayor cantidad de habitantes es del sexo masculino.")
else:
    print("La mayor cantidad de habitantes es del sexo femenino.")

print()

if escolar_mujer == 0:
    print("No hay mujeres en edad escolar.")
else:
    print(f"La cantidad de mujeres en edad escolar es: {escolar_mujer}")

print()

if mayor_hombre == 0:
    print("No hay hombres mayores de 80.")
else:
    print(f"La cantidad de hombres mayores de 80 es: {mayor_hombre}")