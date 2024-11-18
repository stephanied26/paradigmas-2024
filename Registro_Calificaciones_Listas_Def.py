# Registro de Calificaciones:
#***********************************************************************************
# En una clase de programación, los estudiantes realizan varias evaluaciones, cada 
# una con una calificación distinta. Desarrolla un programa que permita registrar y 
# organizar las calificaciones de cada estudiante para luego realizar algunos 
# cálculos básicos.
# El programa debe permitir:
# - Registrar calificaciones: Para cada estudiante, el programa debe almacenar las 
# calificaciones que obtenga en sus evaluaciones. Los estudiantes pueden tener 
# múltiples calificaciones, ya que realizan varias evaluaciones a lo largo del curso.
# - Cálculos y resultados: Calcular y mostrar el promedio de calificaciones de 
# cada estudiante. Determinar y mostrar el nombre del estudiante con la calificación
# más alta de toda la clase (puede ser una calificación obtenida en cualquiera de 
# sus evaluaciones). Mostrar la lista de estudiantes que tienen un promedio de 
# calificaciones superior a 7.
#***********************************************************************************
N = int()
M = int()
nombre = str()
nota = float()
promedio = float()
estudiantes = []
lista_notas = []
promedio_mayor = []
diccionario_notas = {}

def info_alumnos():
    N = int(input("Ingrese cantidad de estudiantes: ")) 
    M = int(input("Ingrese cantidad de notas a registrar: ")) 

    #Ciclo para ingresar datos a la lista y al diccionario
    for i in range(1,N+1): 
        nombre = input(f"\nIngrese el nombre del estudiante: ")
        estudiantes.append(nombre)
        notas_alumno = []
        for j in range(1,M+1):
            nota = float(input(f"Ingrese la nota de la evaluacion {j}: "))
            lista_notas.append(nota) #Notas de todos los estudiantes
            notas_alumno.append(nota) #Notas del alumno
            diccionario_notas[nombre] = notas_alumno
            #dicionario clave: nombre, valor: notas_alumno

    print("\nLista de Alumnos: ",estudiantes)
    print("Notas de cada estudiante: ")
    print(diccionario_notas)

    return diccionario_notas


def promedio_estudiante(diccionario_notas):

    print("\nPromedio de cada estudiante:")
    for estudiante, calificaciones in diccionario_notas.items():
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"{estudiante}: {promedio}")
        # Encontrar estudiantes con promedio mayor a 7.
        if promedio > 7:
            promedio_mayor.append(estudiante)

    print("\nLista de estudiantes que tienen un promedio de calificaciones superior a 7: ")
    print(promedio_mayor)


def mejor_estudiante(diccionario_notas):
    mejor_nota = 0.0
    mejor_estudiante = str
    for estudiante, calificaciones in diccionario_notas.items():
        # Encontrar estudiante con la calificacion mas alta de la clase
        for nota in calificaciones:
            if nota > mejor_nota:
                mejor_estudiante = estudiante
                mejor_nota = nota

    notas_altas = lista_notas.count(mejor_nota) #Cuento si la nota mas alta se repite

    if notas_altas == 1:
        print(f"\nEl estudiante con la nota mas alta es {mejor_estudiante}, con una nota de {mejor_nota}")
    else:
        print("\nHay mas de un estudiante con la nota mas alta.")


def main():
    opcion = 0
    diccionario_notas = info_alumnos()
    while True:
        print("""
        ----------------------------------------------------------------------------
        MENU DE OPCIONES:
        ----------------------------------------------------------------------------                          
        1) Ver Promedio de los estudiantes:
        2) Ver Estudiante con la calificacion mas alta:
        3) Salir del programa.                             
                    """)
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            promedio_estudiante(diccionario_notas)
            input("Ingrese ENTER para continuar.")
        elif opcion == 2:
            mejor_estudiante(diccionario_notas)
            input("Ingrese ENTER para continuar.")
        elif opcion == 3:
            print("El programa ha finalizado.")
            break

main()