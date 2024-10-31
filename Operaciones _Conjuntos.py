# Operaciones con Conjuntos de Números
#***********************************************************************************
# Crea un programa que permita al usuario trabajar con dos conjuntos de números, 
# almacenados en listas. El programa debe ofrecer las siguientes opciones:
# - Agregar números a los conjuntos: El usuario puede agregar números a cada 
#  conjunto, uno por uno.
# - Unión de los conjuntos: Muestra la lista de todos los números que pertenecen 
#  a al menos uno de los dos conjuntos (sin duplicados).
# - Intersección de los conjuntos: Muestra la lista de los números que están 
# presentes en ambos conjuntos.
# - Diferencia entre los conjuntos: Muestra los números que están en el primer 
#  conjunto pero no en el segundo.
# - Salir del programa.
#***********************************************************************************
import os

opcion = str()
N = int()

print("OPERACIONES CON CONJUNTOS DE NUMEROS")

while True:
    print("""
MENU DE OPCIONES:
a) Agregar números a los conjuntos.
b) Unión de los conjuntos.
c) Intersección de los conjuntos.
d) Diferencia entre los conjuntos.
e) SALIR
      """)

    opcion = input("Ingrese opcion: ").upper()
    os.system ("cls")
 
    if opcion == "A":
        conjunto1 = []
        conjunto2 = []
        N = int(input("Ingrese cantidad de numeros que desea agregar al Conjunto 1: "))
        
        print("Ingrese los numeros para el Conjunto 1: ")
        for i in range(N):
            num = int(input("Ingrese un numero: "))
            conjunto1.append(num)

        M = int(input("Ingrese cantidad de numeros que desea agregar al Conjunto 2: "))
        print("Ingrese los numeros para el Conjunto 2: ")
        for j in range(M):
            num = int(input("Ingrese un numero: "))
            conjunto2.append(num)

    elif opcion == "B":
        union = conjunto1+conjunto2
        k = 0
        l = 0
        for k in conjunto1:
            for l in conjunto2:
                if k == l:
                    union.remove(k)
                    union.sort()
        print(conjunto1)
        print(conjunto2)
        print("Unión de los conjuntos: ",union)
        input("Presione ENTER para continuar:")
    elif opcion == "C":
        inter = []
        k = 0
        for k in conjunto1:
            if k in conjunto2:
                inter.append(k)
                inter.sort()
        print(conjunto1)
        print(conjunto2)          
        print("Intersección de los conjuntos: ",inter)
        input("Presione ENTER para continuar:")
    elif opcion == "D":
        diferencia = []
        k = 0
        for k in conjunto1:
            if k not in conjunto2:
                diferencia.append(k)
                diferencia.sort()
        print(conjunto1)
        print(conjunto2)
        print("Numeros que estan en el Conjunto 1 pero no en el Conjunto 2.")
        print("Diferencia entre los conjuntos: ",diferencia)
        input("Presione ENTER para continuar:")
    elif opcion == "E":
        print("El programa ha finalizado.")
        break
    else:
        print("La opcion ingresada no es valida.")
        input("Volver al menu.")
