#ingresar un numero y que imprima un mensaje segun corresponda, si es negativo, positivo o es un 0
# <  >
num = int(input("Ingrese su edad: "))

if num < 0:
    print("Es numero negativo")
elif num > 0:
    print("Es numero positivo")
else:
    print("El numero es cero")