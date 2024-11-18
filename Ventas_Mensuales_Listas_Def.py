# Análisis de Ventas Mensuales por Sucursal:
#***********************************************************************************
# Una tienda registra sus ventas mensuales en diferentes sucursales. Cada venta 
# tiene un monto en pesos y está asociada a una sucursal específica. Se necesita 
# desarrollar un programa para analizar estas ventas y proporcionar información 
# importante a la gerencia.
# El programa debe permitir:
# - Calcular el total de ventas de la tienda: Sumar el monto de todas las ventas 
# realizadas en todas las sucursales y mostrar el total.
# - Identificar la sucursal con mayores ventas acumuladas: Determinar cuál sucursal 
# ha generado el monto total más alto en ventas y mostrar el número de esta 
# sucursal junto con su total acumulado.
# - Calcular el promedio de ventas por sucursal: Para cada sucursal, mostrar el 
# promedio de ventas, considerando todas las ventas registradas para esa sucursal.
# ---------------------------------------------------------------------------------
# Ejemplo de datos:
# Supongamos que la tienda tiene ventas como las siguientes:
#
# Sucursal 1 tuvo una venta de $1000.
# Sucursal 2 tuvo una venta de $1500.
# Sucursal 1 tuvo otra venta de $750.
# Sucursal 3 tuvo una venta de $1200.
# Sucursal 2 tuvo otra venta de $500.
# 
# El programa debería ser capaz de:
# - Sumar el total de todas las ventas.
# - Identificar que la sucursal con mayores ventas acumuladas es la sucursal 2, 
# con $2000.
# - Calcular y mostrar el promedio de ventas de cada sucursal.
#***********************************************************************************
import os

s = int()
opcion = int()
total_ventas = float()
monto = float()
mayor_venta = float()
mayor_sucursal = int()
ventas = []
lista_suma = []
promedio_ventas = float()
diccionario_sucursal = {}
suma_sucursales = {}
promedio_sucursal = {}

def ingresar_datos():
    print("Análisis de Ventas Mensuales por Sucursal:")
    print("Para salir ingrese sucursal -0-")
    input("Presione Enter para continuar:")
    os.system ("cls")

    #Bucle para ingresar Sucursal y monto
    #Agrego items al diccionario_sucursal
    while True:
        s = int(input("Ingrese el numero de sucursal: ")) 
        if s == 0:
            break

        monto = float(input("Ingrese el monto de la venta: ")) 
        ventas.append(monto) #Agrego los montos a la lista ventas.

        # Si la sucursal ya existe, agregamos la venta a la lista
        if s in diccionario_sucursal:
            diccionario_sucursal[s].append(monto)
        # Si la sucursal no existe, la creamos con una lista que contiene la venta
        else:
            diccionario_sucursal[s] = [monto]

    os.system ("cls")
    print("\nDiccionario de sucursales y ventas: ")
    print(diccionario_sucursal)

    return diccionario_sucursal, ventas

def calcular_totalventas(ventas):
    #Sumo el total de ventas
    total_ventas = sum(ventas)

    print("\nEl total de ventas de la tienda es ",total_ventas)

def calcular_ventas_sucursal(diccionario_sucursal):
    # Calcular la suma de ventas por sucursal
    # Guardo las sumas en un nuevo diccionario llamado suma_sucursales
    # Calculo promedio por sucursal y guardo los datos en un diccionario
    for clave, valor in diccionario_sucursal.items():
        suma_sucursales[clave] = sum(valor) #Uso la funcion sum() para sumar los valores
        lista_suma.append(sum(valor)) #Agrego las sumas a una lista

    print("\nDiccionario con la suma de ventas: ")
    print(suma_sucursales)

    return suma_sucursales, lista_suma

def sucursal_mayorVentas(lista_suma, suma_sucursales):
    #Uso la funcion max() para encontrar el mayor valor en la lista suma
    mayor_venta = max(lista_suma) 

    #Busco la clave de la sucursal que tuvo la mayor cantidad de ventas
    for i,j in suma_sucursales.items():
        if j == mayor_venta:
            mayor_sucursal = i

    print("La sucursal que tuvo la mayor cantidad de ventas acumuladas es la sucursal",mayor_sucursal)
    print("con un monto de",mayor_venta)

def calcular_promedio_sucursal(diccionario_sucursal):
    # Calculo promedio por sucursal y guardo los datos en un diccionario
    for clave, valor in diccionario_sucursal.items():
        promedio = sum(valor)/len(valor) #Calculo el promedio
        promedio_sucursal[clave] = promedio 

    print("Promedio de ventas de cada sucursal:")
    print(promedio_sucursal)

def main():

    while True:
        print("""
        ----------------------------------------------------------------------------
        MENU DE OPCIONES:
        ---------------------------------------------------------------------------- 
        1) Ingresar datos.                      
        2) Total de Ventas de la tienda.
        3) Suma de Ventas por Sucursal.
        4) Sucursal con la mayor cantidad de ventas.
        5) Promedio de ventas de cada Sucursal.
        6) Salir del Programa.                           
                    """)
        
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            diccionario_sucursal, ventas = ingresar_datos()
            input("Ingrese ENTER para continuar.")
        elif opcion == 2:
            calcular_totalventas(ventas)
            input("Ingrese ENTER para continuar.")
        elif opcion == 3:
            suma_sucursales, lista_suma = calcular_ventas_sucursal(diccionario_sucursal)
            input("Ingrese ENTER para continuar.")
        elif opcion == 4:
            sucursal_mayorVentas(lista_suma,suma_sucursales)
            input("Ingrese ENTER para continuar.")
        elif opcion == 5:
            calcular_promedio_sucursal(diccionario_sucursal)
            input("Ingrese ENTER para continuar.")
        elif opcion == 6:
            print("El programa ha finalizado.")
            break
        else:
            print("La opcion ingresada no es valida.")

main()