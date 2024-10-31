# GUIA 2 - PUNTO 8
# Ventas por sucursal 
# Ingresar una serie de números por teclado que representan 
# la cantidad de ventas realizadas en las diferentes sucursales de un país de 
# una determinada empresa. Los requerimientos del programa son: 
# Informar la cantidad de ventas ingresadas.
# Total de ventas .
# Cantidad de ventas entre 100 y 300 unidades.
# Cantidad de ventas con 400, 500 y 600 unidades.
# Indicar si hubo una cantidad de ventas inferior a 50 unidades. 
# Usted deberá ingresar cantidad de ventas hasta que se ingrese un valor negativo.

ventas_i = int()
total_ventas = int()
unidades = int()
ventas_100a300 = int()
ventas_400 = int()
ventas_500 = int()
ventas_600 = int()
ventas_50 = int()

while True:
    unidades = int(input("Ingrese las unidades vendidas: "))

    if unidades < 0:
        print("Ha finalizado el ingreso de ventas.")
        break

    total_ventas = total_ventas + unidades
    ventas_i += 1
    
    if unidades < 50:
        ventas_50 += 1
    elif unidades >= 100 and unidades <=300:
        ventas_100a300 += 1
    elif unidades >= 400 and unidades <500:
        ventas_400 += 1
    elif unidades >= 500 and unidades <600:
        ventas_500 += 1
    elif unidades >=600 and unidades <700:
        ventas_600 += 1


print("-----------------------------------------------------------------")
print(f"La cantidad de ventas ingresadas es de:{ventas_i}")
print(f"El total de ventas es de: {total_ventas} unidades")
print(f"Cantidad de ventas entre 100 y 300 unidades: {ventas_100a300}")
print(f"Cantidad de ventas con 400 unidades: {ventas_400}")
print(f"Cantidad de ventas con 500 unidades: {ventas_500}")
print(f"Cantidad de ventas con 600 unidades: {ventas_600}")
print(f"Ventas inferiores a 50 unidades: {ventas_50}")