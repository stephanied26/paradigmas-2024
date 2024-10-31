# GUIA 2 - PUNTO 3
# Sueldos y aguinaldo
# Ingresar por teclado los sueldos de un vendedor, correspondientes al primer 
# semestre del año y luego:
# a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
# b) Determinar en qué mes recibió el sueldo más bajo del período.
# c) Informar el sueldo promedio del semestre.

sueldo = float()
suma_sueldo = float()
aguinaldo = float()
mayor_sueldo = float(0)
menor_sueldo = float(0)
menor_mes = int(0)
mes = int()
promedio = float()

print("Programa para calcular aguinaldo del Primer Semestre:")

for mes in range (1,7):
    sueldo = float(input(f"Ingrese el sueldo del mes {mes}:"))

    # Acumulador de los sueldos del semestre
    suma_sueldo = suma_sueldo + sueldo

    # Si es el primer mes asigno los primeros valores a las variables
    if mes == 1:
        mayor_sueldo = sueldo
        menor_sueldo = sueldo
        menor_mes = mes
    
    #Calcular mayor y menor sueldo
    if sueldo < menor_sueldo:
        menor_sueldo = sueldo
        menor_mes = mes
    elif sueldo > mayor_sueldo:
        mayor_sueldo = sueldo

#Calcular aguinaldo y promedio del sueldo
aguinaldo = mayor_sueldo /2
promedio = suma_sueldo /6

#Mostrar datos por pantalla
print("-------------------------------------------------------------------")
print(f"El aguinaldo correspondiente de este semestre es de: ${aguinaldo}")
print(f"El mes con el sueldo mas bajo: Mes {menor_mes}")
print(f"El sueldo promedio del semestre es de: ${promedio}")