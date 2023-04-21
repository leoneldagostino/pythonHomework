'''
1. 
Crear una funcion que convierta grados celsius a grados fahrenhei.
Recibe un parametro(grados Celsius) y devuelve el resultado en grados Fahrenheit.

Leonel D'agostino 1H

'''


def celsius_to_fahrenheit(grado):
    resultado_fahrenheit = grado * 1.8 + 32
    print("El resultado de {}° Celsius a fahrenheit es: {}° Fahrenheit.".format(grado,resultado_fahrenheit))
    
grados = int(input("Ingrese los grados Celcius que quiere convertir a Fahrenheit: "))

celsius_to_fahrenheit(grados)

