# Análisis de Rendimiento en una Carrera de Autos
#************************************************************************************
# En una carrera de autos, cada vehículo registra sus tiempos en varias vueltas a lo 
# largo de la competencia. Cada auto tiene un número de identificación único, y se 
# quiere analizar su rendimiento en función de sus tiempos de vuelta.
# Desarrolla un programa que permita registrar los tiempos de cada auto y realizar 
# algunos análisis de rendimiento al final de la carrera.
# El programa debe poder:
# - Registrar tiempos de vuelta para cada auto: A medida que los autos completan 
# vueltas, se debe almacenar el tiempo en segundos de cada vuelta. Si un auto 
# registra múltiples tiempos, todos deben ser guardados para calcular estadísticas 
# al final.
# - Calcular el tiempo promedio de vuelta para un auto específico: Dado el número 
# de identificación de un auto, calcula y muestra el tiempo promedio de sus vueltas.
# - Determinar el auto más rápido: Identifica el auto con el menor tiempo promedio 
# de vuelta y muestra su número de identificación y su tiempo promedio.
# - Mostrar el rendimiento de todos los autos: Muestra el número de identificación 
# de cada auto junto con todos sus tiempos de vuelta registrados.
#************************************************************************************
N = int()
M = int()
diccionario_autos = {}
diccionario_promedios = {}
opcion = int()

def info_autos():
    N = int(input("Ingrese cantidad de autos: ")) 
    M = int(input("Ingrese cantidad de ciclos a registrar: ")) 

    #Ciclo para ingresar datos a la lista y al diccionario
    for i in range(N): 
        auto = input(f"\nIngrese el numero de identificacion del auto: ")
        tiempos_auto = [] #Lista que va a contener todos los tiempos de cada auto
        for j in range(M):
            tiempo = int(input(f"Ingrese el tiempo de vuelta en segundos del auto {auto}: "))
            tiempos_auto.append(tiempo) #Tiempos del auto
            diccionario_autos[auto] = tiempos_auto
            #dicionario clave: auto, valor: tiempos_auto

    print("Tiempos de cada auto: ")
    print(diccionario_autos)

    return diccionario_autos

def promedio_auto(diccionario_autos):

    print("\nPromedio de cada auto:")
    for auto, tiempos in diccionario_autos.items():
        promedio = sum(tiempos) / len(tiempos)
        diccionario_promedios[auto] = promedio
        print(f"{auto}: {promedio}")

    return diccionario_promedios

def auto_mas_rapido(diccionario_promedios):
    contador = 0
    for auto, promedio in diccionario_promedios.items():
        contador += 1
        if contador == 1:
            mejor_promedio = promedio #Guarda el primer promedio como mejor promedio
            mejor_auto = auto #Guarda el primer auto como mejor auto
        else:
            if promedio < mejor_promedio:
                mejor_promedio = promedio
                mejor_auto = auto

    print(f"El auto mas rapido es el numero {mejor_auto}, con un promedio de {mejor_promedio:.2f}")

def main():
    
    while True:
        print("""
        ----------------------------------------------------------------------------
        MENU DE OPCIONES:
        ---------------------------------------------------------------------------- 
        1) Registrar tiempos                       
        2) Ver Promedio de tiempo:
        3) Ver Auto mas rapido:
        4) Salir del programa.                             
                    """)
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            diccionario_autos = info_autos()
            input("Ingrese ENTER para continuar.")
        elif opcion == 2:
            diccionario_promedios = promedio_auto(diccionario_autos)
            input("Ingrese ENTER para continuar.")
        elif opcion == 3:
            auto_mas_rapido(diccionario_promedios)
            input("Ingrese ENTER para continuar.")
        elif opcion == 4:
            print("El programa ha finalizado.")
            break

main()