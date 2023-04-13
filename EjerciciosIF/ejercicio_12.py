#Ingresar 2 numeros y imprimir si el primero es positivo, o si el segundo es positivo o que los dos son negativos en caso de ser
#<  >

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > 0 and num2 < 0:
    print("El primer numero es positivo")
elif num2 > 0 and num1 < 0:
    print("El segundo numero es positivo")
else:
    print("Los dos numeros son negativos")