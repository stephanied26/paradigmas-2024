# GUIA 2 - PUNTO 2
# Secuencia de impares
# Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos 
# entre ellos, en forma ascendente y descendente

num1 = 0
num2 = 0

print("Ingresar dos numeros diferentes entre si: ")
num1 = int(input("Ingrese el primer numero: ")) 
num2 = int(input("Ingrese el segundo numero: ")) 

while num1 == num2:
    print("Los numeros ingresados son iguales. Intente de nuevo.\n")
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

if num1<num2:
    primero = num1 
    ultimo = num2 
else:
    primero = num2
    ultimo = num1 

print("Los numeros impares que se encuentran entre esos numeros son: ")

print("Ascendente:")
for i in range(primero, ultimo+1):
    if i%2!=0:
        print (i)

print()

print("Descendente:")
for j in range(ultimo, primero-1,-1):
    if j%2!=0:
        print (j)
