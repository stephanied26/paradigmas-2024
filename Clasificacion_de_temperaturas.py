#EJERCICIO 1 - Clasificacion de Temperaturas.

#Definir variables
temperatura = float();
categoria = str();

#Ingreso de datos
temperatura = float(input("Ingrese una temperatura en grados Celsius: "))

#Validacion de datos
while temperatura > 55:
    print ("Error. Ingrese una temperatura en Grados Celsius: ")
    temperatura = float(input(""))

#Determinar la categoria de la temperatura ingresada
if temperatura < 0:
    categoria = "Congelante"
elif temperatura <= 15:
    categoria = "Fria"
elif temperatura <= 25:
    categoria = "Templada"
else:
    categoria = "Calida"

#Mostrar por pantalla la categoria
print ("La temperatura es",categoria)
