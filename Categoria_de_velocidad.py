# PARADIGMAS DE PROGRAMACION - 2do Cuatrimestre - 2024
#**********************************************************************************
# EJERCICIO: Categoría de Velocidad
#****************************************************************************************************
# Descripción: Imagina que estás desarrollando un software para un club de corredores que desea 
# clasificar el rendimiento de sus miembros según la velocidad promedio de una carrera reciente. 
# El objetivo es determinar en qué categoría de velocidad se encuentra un corredor y proporcionar 
# la clasificación adecuada. El programa pedirá al usuario que introduzca la distancia recorrida 
# en kilómetros y el tiempo tomado en minutos. Con esta información, se calculará la velocidad 
# promedio. Dependiendo de cuán alta o baja sea esta velocidad, el corredor puede ser clasificado 
# como alguien que tiene un ritmo más lento, moderado o rápido. Deberás mostrar esta clasificación 
# al usuario, dejando que las circunstancias de la velocidad determinen la categoría.
#****************************************************************************************************

#Definir Variables
kilometros = int;
minutos = int;
velocidad_total = float;
velocidad = float;
promedio = float;
continuar = str;
iniciar = bool;
i = int;

#Inicializar variables
kilometros = 0;
minutos = 0;
velocidad_total = 0.0;
velocidad = 0.0;
promedio = 0.0;
continuar = "";
iniciar = True;
i = 1;
 
#En cada Ciclo While se ingresan los datos de cada corredor.
while iniciar == True:
    #Ingreso de Datos
    kilometros = int(input("Ingrese la distancia recorrida en kilometros: "));
    minutos = int(input("Ingrese el tiempo en minutos: "));

    velocidad = (kilometros/minutos)*60; #Calculo Velocidad en kilometros por hora del corredor.
    velocidad_total = velocidad_total + velocidad; #Acumular Velocidad Total de los corredores.
    promedio = velocidad_total / i; #Calcular promedio de velocidad.
        
    #Mostrar Datos por Pantalla
    print ("\nEl corredor numero", i, "tiene una velocidad de", velocidad, "km/h.");

    #Determinar Categoria de Velocidad
    if velocidad < promedio:
        print ("Ritmo de velocidad: mas lento que el promedio.\n");
    elif velocidad > promedio:
        print ("Ritmo de velocidad: mas rapido que el promedio.\n");
    else:
        print ("Ritmo de velocidad: moderado\n");

    #Preguntar al usuario si desea continuar
    print ("Desea ingresar los datos de otro corredor?");
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

print ("\nPrograma Finalizado.")