# PARADIGMAS DE PROGRAMACION - 2do Cuatrimestre - 2024
#*****************************************************************************************************
# EJERCICIO: Sistema de Control de Inventario
#*****************************************************************************************************
# Descripción: Estás creando un sistema para controlar el inventario de una tienda. La tienda tiene 
# una lista de productos y sus respectivas cantidades en stock. El programa debe permitir al usuario 
# ingresar una serie de transacciones diarias, donde cada transacción puede ser una compra o una venta 
# de un producto. 
# El programa debe solicitar al usuario que ingrese el nombre del producto y si es una compra o una venta.
# Si es una compra, se debe incrementar la cantidad de ese producto en el inventario; si es una venta, 
# se debe verificar si hay suficiente cantidad en el stock antes de realizar la transacción. 
# Si no hay suficientes productos en stock, el programa debe mostrar un mensaje adecuado. A lo largo del 
# día, el sistema debe procesar varias transacciones y, al final, mostrar un resumen del inventario con 
# las cantidades finales de cada producto.
#*******************************************************************************************************
producto = str();
cantidad = int();
opcion = int();
cuaderno = 10;
mochila = 12;
cartuchera = 15;
agenda = 20;
continuar = str();
iniciar = True;

while iniciar == True:

    print ("\n Ingrese el nombre de un producto del inventario: ");
    print (" - Cuaderno.");
    print (" - Mochila.");
    print (" - Cartuchera.");
    print (" - Agenda.");
    print ("");

    producto = input().lower();
    cantidad = int(input("\nIngrese cantidad: "));

    print ("Seleccione -1- para COMPRA o -2- para VENTA: ");
    opcion = int(input());

    while opcion != 1 and opcion != 2:
        print ("Error. Ingrese un valor valido.");
        print ("Seleccione -1- para COMPRA o -2- para VENTA: ");
        opcion = int(input());

    if opcion == 1:
        if producto == "cuaderno":
            print ("Usted ha comprado",cantidad,"cuadernos.")
            cuaderno = cuaderno + cantidad;
        elif producto == "mochila":
            print ("Usted ha comprado",cantidad,"mochilas.")
            mochila = mochila + cantidad;
        elif producto == "cartuchera":
            print ("Usted ha comprado",cantidad,"cartucheras.")
            cartuchera = cartuchera + cantidad;
        elif producto == "agenda":
            print ("Usted ha comprado",cantidad,"agendas.")
            agenda = agenda + cantidad;
        else:
            print ("El producto no forma parte del inventario.");

    else:
        if producto == "cuaderno":
            if cuaderno < cantidad:
                print ("No hay suficientes cuadernos en stock.");
            else:
                print ("Usted ha vendido",cantidad,"cuadernos.")
                cuaderno = cuaderno - cantidad;
        elif producto == "mochila":
            if mochila < cantidad:
                print ("No hay suficientes mochilas en stock.");
            else:
                print ("Usted ha vendido",cantidad,"mochilas.")
                mochila = mochila - cantidad;
        elif producto == "cartuchera":
            if cartuchera < cantidad:
                print ("No hay suficientes cartucheras en stock.");
            else:
                print ("Usted ha vendido",cantidad,"cartucheras.");
                cartuchera = cartuchera - cantidad;
        elif producto == "agenda":
            if agenda < cantidad:
                print ("No hay suficientes agendas en stock.");
            else:
                print ("Usted ha vendido",cantidad,"agendas.");
                agenda = agenda - cantidad;
        else:
            print ("El producto no forma parte del inventario.");
    
    print ("\nDesea realizar una nueva transaccion?: ");
    print ("Ingrese 'S' para si o 'N' para no.");
    continuar = input().lower();

    #Validacion de datos
    while continuar != "s" and continuar != "n":
        print ("Error. Seleccione 'S' para si o 'N' para no: ");
        continuar = input().lower();

    if continuar == "n":
        iniciar = False;
    else:
        iniciar = True;

#RESUMEN
print("\nLISTA DE PRODUCTOS Y SUS CANTIDADES EN STOCK: ");
print (" Cuaderno:",cuaderno);
print (" Mochila:",mochila);
print (" Cartuchera:",cartuchera);
print (" Agenda:",agenda);
