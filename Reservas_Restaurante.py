# PARADIGMAS DE PROGRAMACION - 2do Cuatrimestre - 2024
#*****************************************************************************************************
# EJERCICIO: Sistema de Gestión de Reservas en un Restaurante
#*****************************************************************************************************
# Descripción: Eres el encargado de desarrollar un sistema que permite al personal de un restaurante 
# gestionar las reservas de mesas. El sistema debe verificar la disponibilidad de mesas para un grupo 
# de personas y procesar varias reservas en el transcurso de un día.
# El programa debe solicitar al usuario que ingrese el tamaño del grupo y, según la cantidad de personas,
# determinar si hay una mesa disponible. El restaurante tiene mesas para 2, 4, 6 y 8 personas, y cada
# mesa solo puede ser asignada si el número de personas del grupo es igual o menor a la capacidad de 
# la mesa. A lo largo del día, se recibirán múltiples solicitudes, y el sistema deberá manejar varias 
# reservas mientras asegura que no se sobrepase la capacidad de cada mesa. Además, si el grupo es 
# demasiado grande o pequeño para las mesas disponibles, el programa debe indicar que no hay mesa para 
# ese grupo.
#*****************************************************************************************************
Mesa2 = bool ();
Mesa4 = bool ();
Mesa6 = bool ();
Mesa8 = bool ();
grupo = int ();
continuar = str();
iniciar = True;

while iniciar == True:

    grupo = int(input("\nIngrese el tamaño del grupo: "));

    if grupo > 8 or grupo == 0:
        print ("No hay mesas para ese grupo de personas.");
    elif grupo <= 2 and Mesa2 is False:
        print ("Mesa para 2: Reservada.");
        Mesa2 = True;
    elif grupo <= 4 and Mesa4 is False:
        print ("Mesa para 4: Reservada.");
        Mesa4 = True;
    elif grupo <= 6 and Mesa6 is False:
        print ("Mesa para 6: Reservada.");
        Mesa6 = True;
    elif grupo <=8 and Mesa8 is False:
        print ("Mesa para 8: Reservada.");
        Mesa8 = True;
    else:
        print("Todas las mesas ya están reservadas. Intente más tarde.");
    
    print ("\nDesea ingresar nuevo grupo?: ");
    print ("Ingrese 'S' para si o 'N' para no.");
    continuar = input().lower();

    #Validacion de datos
    while continuar != "s" and continuar != "n":
        print ("Error. Seleccione 'S' para si o 'N' para no: ")
        continuar = input().lower();

    if continuar == "n":
        iniciar = False;
    else:
        iniciar = True;

print("\nPrograma finalizado.");