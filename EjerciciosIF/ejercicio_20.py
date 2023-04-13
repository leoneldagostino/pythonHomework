# Ingresar 2 numero que los cuales imprima cual es el mayor o si son iguales

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 < num2:
    print("El segundo numero es mayor")
elif num1 > num2:
    print("El primer numero es mayor")
else:
    print("Los dos numeros son iguales")