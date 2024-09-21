#EJERCICIO 2 - Calculadora de Descuentos

#Definir variables
precio = float();
precio_final = float();
descuento = float();

#Ingreso de datos
precio = float(input("Ingresar precio del producto: "));

#Validacion de datos
while precio <= 0:
    print ("Error. Ingrese un valor valido: ");
    precio = float(input(""));

#Definir descuento a aplicar
if precio < 50:
    precio_final = precio
    print ("El monto no alcanza para obtener un descuento.");
elif precio <= 100:
    descuento = precio*0.10
    precio_final = precio - descuento
    print ("El descuento a aplicar es del 10% ");
else:
    descuento = precio*0.20
    precio_final = precio - descuento
    print ("El descuento a aplicar es del 20% ");

#Mostrar precio final luego de aplicar el descuento
print ("El precio final es de", precio_final);