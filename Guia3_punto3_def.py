#////////////////////////////////////////////////////////////////////////////////////
# GUIA 3 - PUNTO 3
#////////////////////////////////////////////////////////////////////////////////////
# Menu de Opciones con secuencias:
# Escribir un programa que le permita al usuario, a través de un menú de opciones, 
# las siguientes operaciones: 
# a) Generar una serie n de números (n ingresado por teclado y validando que sea 
# mayor a cero) y mostrar la suma de los cuadrados. 
# b) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras 
# que finalizan con vocales.
# c) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay 
# mayor cantidad de valores pares o de impares.
# d) Salir
#////////////////////////////////////////////////////////////////////////////////////

opcion = str()
N = int(-1)
cuadrado = int()
suma = int()
total_num = int()
palabra = int()
num = int()
par = int()
impar = int()

def suma_cuadrados():
    suma = 0
    numero = 0
    cuadrado = 0

    N = int(input("Ingrese una cantidad de numeros: "))

    while N <= 0:
        print("Error. Ingrese un valor valido.")
        N = int(input("Ingrese cantidad de numeros a ingresar: "))
        
    for i in range(1,N+1):
        numero = int(input(f"\nIngrese el numero {i}: "))
        cuadrado = numero * numero
        suma = suma + cuadrado
        print (f"El cuadrado de {numero} es: {cuadrado}")
            
    print(f"\nLa suma de los cuadrados es: {suma}")

def ingresar_texto():
    palabra = 0
    texto = input("Ingrese un texto: ")

    #Bucle para determinar si el texto finaliza con un punto.
    while texto[-1] != '.':
        print("El texto debe finalizar con un punto.")
        texto = input("Ingrese un texto: ")
        
    #Bucle para determinar si la ultima palabra del texto termina en vocal
    if texto[-2] in 'aeiou':
        palabra=palabra+1

    # Dividimos el texto en palabras usando la función split()
    palabras = texto.split()

    # Bucle For para buscar en cada palabra. Si la ultima letra i[-1] es alguna vocal 
    # se incrementa el contador.
    for i in palabras:
        if i[-1] in 'aeiou':
            palabra=palabra+1

    print(f"Cantidad de palabras que finalizan en vocal: {palabra}")

def ingresar_numeros():
    num = -1
    par = 0
    impar = 0
    print("Para finalizar ingrese CERO (0)")

    while True:
        num = int(input("Ingresar un numero: "))
        if num == 0:
            break

        if num%2 == 0:
            par = par + 1
        else:
            impar = impar + 1
        
    if par == impar:
        print("\nHay igual cantidad de numeros pares e impares.")
    elif par > impar:
        print("\nHay mayor cantidad de numeros pares.")
    else:
        print("\nHay mayor cantidad de numeros impares.")

    print(f"Cantidad de numeros pares: {par}")
    print(f"Cantidad de numeros impares: {impar}")

def main():
    
    while True:
        print("""
        ---------------------------------------------------------------------------------
        MENU DE OPCIONES:
        ---------------------------------------------------------------------------------
        a) Ingresar numeros y mostrar la suma de los cuadrados.
        b) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras
        que finalizan con vocales.
        c) Ingresar numeros y determinar si hay mayor cantidad de valores pares o impares. 
        La carga finaliza con CERO (0)
        d) SALIR
        """)

        opcion = input().upper()

        if opcion == "A":
            suma_cuadrados()
            input("\nIngrese ENTER para continuar.")
        elif opcion == "B":
            ingresar_texto()
            input("\nIngrese ENTER para continuar.")
        elif opcion == "C":
            ingresar_numeros()
            input("\nIngrese ENTER para continuar.")
        elif opcion == "D":
            print("\nEl programa ha finalizado.")
            break
        else:
            print("\nLa opcion ingresada no es valida.")

#Llamo a la funcion main para empezar a ejecutar el programa
main()