# Analisis de Numeros
#***********************************************************************************
# Crear un programa que permita almacenar una lista de números enteros y 
# realizar diferentes análisis sobre ellos. El programa debe ofrecer las 
# siguientes opciones:
# - Agregar número a la lista: 
#   El usuario puede agregar un número a la lista de números.
# - Mostrar el número mayor y el número menor: El programa muestra el número 
#   más grande y el más pequeño de la lista.
# - Calcular la suma y el promedio: El programa debe calcular y mostrar la suma 
#   de todos los números y el promedio.
# - Contar cuántos números son pares: Muestra cuántos números en la lista son pares.
# - Salir del programa.
#***********************************************************************************
import os

opcion = str()
lista_num = []
par_num = []
num = int()
suma = int()
promedio = float()

print("ANALISIS DE NUMEROS")

while True:
    print("""
MENU DE OPCIONES:
a) Agregar número a la lista.
b) Mostrar el número mayor y el número menor.
c) Calcular la suma y el promedio.
d) Contar cuántos números son pares
e) SALIR
      """)

    opcion = input("Ingrese opcion: ").upper()
    os.system ("cls")

    if opcion == "A":
        N = int(input("Ingrese cantidad de numeros que desea agregar: "))

        for i in range(N):
            num = int(input("Ingrese un numero: "))
            lista_num.append(num)

        print("Lista de numeros: ",lista_num)
        input("Presione ENTER para continuar:")
    elif opcion == "B":
        print(lista_num)
        print("El numero menor de la lista es: ",min(lista_num))
        print("El numero mayor de la lista es: ",max(lista_num))
        input("Presione ENTER para continuar:")
    elif opcion == "C":
        suma = sum(lista_num)
        promedio = suma / len(lista_num)
        print(lista_num)
        print("La suma de los numeros de la lista es: ",suma)
        print(f"El promedio de los numeros de la lista es: {promedio:.2f}")
        input("Presione ENTER para continuar:")
    elif opcion == "D":
        par = 0
        for numero in lista_num:
            if numero %2 == 0:
                par_num.append(numero)
                par+=1
        print("La cantidad de numeros pares de la lista es: ",par)
        print("Los numeros pares son: ",par_num)
        input("Presione ENTER para continuar:")
    elif opcion == "E":
        print("El programa ha finalizado.")
        break
    else:
        print("La opcion ingresada no es valida.")
        input("Volver al menu.")