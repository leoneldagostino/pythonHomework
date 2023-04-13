#ingresar un numero y imprimir que sea par y multiplo de 3 

num = int(input("Ingrese un numero: "))

if num % 2 == 0 and num % 3 == 0:
    print("El numero es par y multiplo de 3")
else:
    print("El numero no cumple con las condiciones")