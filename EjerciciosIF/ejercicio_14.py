# ingresar un numero y imprimir si es multiplo de 4 y 6

num = int(input("Ingrese un numero: "))

if num % 6 == 0 and num % 4 == 0:
    print("Es multiplo de 6 y de 4")
else:
    print("No es multiplo de 6 y 4")