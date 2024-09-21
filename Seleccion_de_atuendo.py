# PARADIGMAS DE PROGRAMACION - 2do Cuatrimestre - 2024
#**********************************************************************************
# EJERCICIO: Selección de Atuendo
#*****************************************************************************************************
# Estás diseñando una aplicación que ayuda a las personas a elegir su atuendo diario basado en 
# la temperatura y la posibilidad de lluvia. La aplicación debe hacer recomendaciones sobre qué 
# tipo de ropa y accesorios son apropiados para el día. La aplicación pedirá al usuario que 
# introduzca la temperatura en grados Celsius y si espera lluvia o no. 
# Basado en la información ingresada, deberás decidir si el atuendo debe incluir algo más abrigado
# o más ligero, y si es necesario agregar algún accesorio adicional para protegerse del clima. 
# Al final, deberás mostrar la recomendación completa al usuario, considerando tanto la temperatura 
# como la posibilidad de lluvia.
#******************************************************************************************************

#Definir Variables
temperatura = float;
lluvia = int;

#Inicializar Variables
temperatura = 0.0;
lluvia = 0;

#Ingreso de Datos
temperatura = float(input("Ingrese una temperatura en grados Celsius: "));
lluvia = int(input("Ingrese probabilidad de lluvia del 0 al 100%: "));

#Validacion de Datos
while temperatura > 55:
    print ("Error. Ingrese una temperatura en Grados Celsius: ")
    temperatura = float(input(""))

while lluvia < 0 or lluvia > 100:
    print ("Error. Ingrese probabilidad de lluvia del 0 al 100%: ");
    lluvia = int(input(""));

#Determinar atuendo segun la temperatura ingresada
if temperatura < 0:
    print("\nAtuendo recomendado: Campera abrigada, pantalon largo, botas, bufanda, guantes.");
elif temperatura <= 15:
    print("\nAtuendo recomendado: Campera abrigada, pantalon largo, bufanda.");
elif temperatura <= 25:
    print("\nAtuendo recomendado: Campera ligera, pantalon largo.");
else:
    print("\nAtuendo recomendado: Remera, pantalon corto.");

#Determinar accesorios en caso de lluvia.
if lluvia == 0:
    print("No hay probabilidad de lluvia.");
    print("No se necesitan accesorios.");
elif lluvia <= 30:
    print("Probabilidad de lluvia baja.");
    print("Accesorio recomendado: Piloto ligero.");
elif temperatura <= 60:
    print("Probabilidad de lluvia media.");
    print("Accesorio recomendado: Paraguas.");
else:
    print("Probabilidad de lluvia alta.");
    print("Accesorios recomendados: Piloto, Botas de lluvia, Paraguas.");
