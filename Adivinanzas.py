# PARADIGMAS DE PROGRAMACION - 2do Cuatrimestre - 2024
#**********************************************************************************
# EJERCICIO: Adivinanzas
#***********************************************************************************
# Escribe un programa en el que el usuario deba adivinar un número secreto generado
# aleatoriamente entre 1 y 100. El usuario tendrá un total de 10 intentos para 
# lograrlo. Después de cada intento, el programa le indicará si el número ingresado
# es mayor o menor que el número secreto. Además, el programa llevará un contador de
# los intentos restantes y lo mostrará en cada intento. Si el usuario acierta antes 
# de que se le acaben los intentos, el programa lo felicitará y terminará. En caso 
# contrario, una vez agotados los intentos, el programa deberá revelar el número 
# secreto y mostrar un mensaje de derrota.
#***********************************************************************************
import random;
import os;

numero = int();
numero_secreto = int();
continuar = str();

print ("""
*********************************************
***** Bienvenido a JUEGO DE ADIVINANZAS *****
*********************************************
Usted debe adivinar el numero secreto, el 
cual se encuentra entre el 1 y el 100.
*********************************************
Tiene 10 intentos para lograrlo.
Buena Suerte!
********************************************* """);

input("Presione ENTER para continuar");
os.system ("cls");
iniciar = True;

while iniciar == True:
    intentos = 10;
    numero_secreto = random.randint(1,100);
    print (numero_secreto);

    for i in range (0,10):
        intentos-=1; # Utilizo un decrementador para restar de a uno los intentos.
        numero = int(input("\nIngrese un numero del 1 al 100: "));

        while numero <= 0 or numero > 100:
            print ("\nError. Ingrese un valor valido");
            numero = int(input("Ingrese un numero del 1 al 100: "));
        
        if intentos == 0 and numero != numero_secreto:
            print("\nJuego Terminado.");
            print("No pudo adivinar el numero secreto.")
            print("El numero secreto era: ",numero_secreto);
            break;
        
        if numero == numero_secreto:
            print("\n************************************************");
            print("Felicitaciones! Has adivinado el numero secreto.");
            print("El numero secreto es: ",numero_secreto);
            print("************************************************");
            break;
        elif numero > numero_secreto:
            print ("\nEl numero ingresado es mayor que el numero secreto.");
            print ("Tiene",intentos,"intento/s restante/s.");
        elif numero < numero_secreto:
            print ("\nEl numero ingresado es menor que el numero secreto.");
            print ("Tiene",intentos,"intento/s restante/s.");
        

    print ("\nDesea continuar jugando?: ");
    print ("Seleccione 'S' para si o 'N' para no: ");
    continuar = input().lower();

    while continuar != "s" and continuar != "n":
        print ("Error. Seleccione 'S' para si o 'N' para no: ")
        continuar = input().lower();

    if continuar == "n":
        iniciar = False;
    else:
        iniciar = True;
    
    os.system ("cls");
        
print("\nHasta la proxima!");