#ingresar un numero que va imprimir si es par y positivo o imprimira que no cumple ninguna condicion

num = int(input("Ingrese un numero: "))

if num > 0  and num % 2 == 0:
    print("Es un numero par y positivo")
else:
    print("No cumple con ninguna de las dos condiciones")