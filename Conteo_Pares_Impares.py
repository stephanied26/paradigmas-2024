# PARADIGMAS DE PROGRAMACION - 2do Cuatrimestre - 2024
#**********************************************************************************
# EJERCICIO: Conteo de Números Pares e Impares
#**********************************************************************************
# Descripción: Imagina que estás diseñando un contador para analizar una serie de 
# números. Este programa debe ser capaz de procesar varios números y contar cuántos 
# de ellos son pares y cuántos son impares. 
# El programa solicitará al usuario que ingrese una cantidad de números. A medida 
# que se vayan introduciendo, se debe llevar un registro de cuántos son pares y 
# cuántos son impares. Al final del proceso, se mostrará un resumen indicando 
# cuántos números pares e impares fueron ingresados. El programa deberá continuar 
# contando mientras se sigan ingresando números.
#***********************************************************************************

#Definir Variables
par = int;
impar = int;
numero = int;
continuar = str;
iniciar = bool;

#Inicializar Variables
par = 0;
impar = 0;
numero = 0;
continuar = "";
iniciar = True;

while iniciar == True:
    #Ingreso de Datos.
    numero = int(input("Ingrese un numero entero positivo: "));

    #Validacion de Datos.
    while numero < 0:
        print ("Error. Ingrese un valor valido");
        numero = int(input("Ingrese un numero entero positivo: "));

    if numero % 2 == 0:
        par += 1;
    else:
        impar += 1;

    #Preguntar al usuario si desea continuar
    print ("\nDesea ingresar otro numero?");
    print ("Seleccione 'S' para si o 'N' para no: ");
    continuar = input().lower();

    #Validacion de datos
    while continuar != "s" and continuar != "n":
        print ("Error. Seleccione 'S' para si o 'N' para no: ")
        continuar = input().lower();

    if continuar == "n":
        iniciar = False;
    else:
        iniciar = True;

#Mostrar por pantalla los resultados
print ("\nLa cantidad de numero pares ingresados es: ", par);
print ("La cantidad de numeros impares ingresados es: ", impar);
