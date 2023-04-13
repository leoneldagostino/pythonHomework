#ingresar un numero y tiene que imprimir si es divisible por 3 y 5

num = int(input("Ingrese un numero: "))

if num % 3 == 0 and num % 5 == 0:
    print("El numero es divisible por 3 y 5")
else:
    print("Los numeros no son divisibles por 3 y 5")