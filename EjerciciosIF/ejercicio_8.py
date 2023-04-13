#Pedir un numero y que imprima si es un cuadrado perfecto o no

numero = int(input("Ingrese un numero positivo: "))
numero_cuadrado = numero**0.5


if numero_cuadrado % 1 == 0:
    print("Es un cuadrado perfecto")
else:
    print("No es un cuadrado perfecto")

