'''
2.
Crear una función que calcule el área de un círculo.
Recibe un parámetro (radio) y devuelve el área del círculo.

'''
import math

def calcular_area_circulo(radio):
    resultado_area = math.pi * radio** 2 
    print("El resultado del calculo del area del circulo es: {} ".format(resultado_area))
    
radio = int(input("Ingrese el radio para poder calcular el area del circulo: "))

calcular_area_circulo(radio)