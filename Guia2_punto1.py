# GUIA 2 - PUNTO 1
# Ciclistas:La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).
# Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. 
# Luego se pide:
# a) Determinar y mostrar el nombre del ganador de la carrera.
# b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo 
# del ganador es menor al tiempo record, mostrar un mensaje.
# c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.

mejor_tiempo = 0
competidor = 0
tiempo_total = 0
tiempo = 0
record = 0
nombre = ""
ganador = ""

N = int(input("Ingrese la cantidad de competidores: "))


for i in range(N):
    competidor = competidor + 1
    nombre= input(f"Ingrese el nombre del competidor {competidor}: ")
    tiempo= int(input("Ingrese el tiempo de carrera en segundos: "))
    tiempo_total = tiempo_total + tiempo

    if competidor == 1:
       mejor_tiempo = tiempo
    
    if tiempo<mejor_tiempo:
        mejor_tiempo = tiempo
        ganador = nombre

print(f"El ganador es {ganador}\n")

record = int(input("Ingrese el tiempo record registrado para esta carrera: "))

if record > mejor_tiempo:
    print(f"{ganador} ha logrado un nuevo record!\n")
else:
    print("Nadie ha logrado superar el record en esta ocasion.\n")

print("El promedio de tiempo es: ", tiempo_total/competidor)




