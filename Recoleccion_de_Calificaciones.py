# PARADIGMAS DE PROGRAMACION - 2do Cuatrimestre - 2024
#**********************************************************************************
# EJERCICIO: Recolección de Calificaciones
#**********************************************************************************
# Descripción: Estás creando una herramienta que ayuda a los estudiantes a llevar 
# un registro de sus calificaciones y obtener su promedio. El objetivo de la 
# aplicación es permitir que el estudiante ingrese varias calificaciones una por 
# una y luego calcule el promedio de todas ellas. 
# El programa debe pedir al usuario que ingrese las calificaciones de manera 
# secuencial. Una vez que se hayan ingresado todas las notas, deberá calcular y 
# mostrar el promedio al estudiante. Asegúrate de que el programa permita ingresar 
# varias calificaciones sin que se detenga antes de tiempo y que el promedio sea 
# calculado correctamente cuando el usuario decida finalizar.
#***********************************************************************************

#Definir variables
calificacion = float;
calificacion_suma = float;
promedio = float;
continuar = str;
iniciar = bool;
i = int;

#Inicializar variables
calificacion = 0.0;
calificacion_suma = 0.0;
promedio = 0.0;
continuar = "";
iniciar = True;
i = 1;

#En cada Ciclo While se ingresa una calificacion mientras que iniciar = True.
while iniciar == True:
    #Ingreso de Datos.
    calificacion = float(input("Ingrese la calificacion: "));

    #Validacion de Datos.
    while calificacion <= 0:
        print ("Error. Ingrese un valor valido.");
        calificacion = float(input("Ingrese la calificacion: "));

    #Sumar calificaciones y calcular promedio.
    calificacion_suma = calificacion_suma + calificacion;
    promedio = calificacion_suma / i;

    #Preguntar al usuario si desea continuar
    print ("\nDesea ingresar otra calificacion?");
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
    
    i = i + 1;

print ("\nEl estudiante tiene un promedio de: " , promedio);