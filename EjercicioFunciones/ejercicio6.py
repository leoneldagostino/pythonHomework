'''
6.
Crear una función que calcule el área de un triángulo. 
Recibe dos parámetros (base y altura) y devuelve el área.

'''


def calcular_area(base,altura):
    area = altura * base / 2
    print("El area del triangulo es: {} ".format(area))
    

base = int(input("Ingrese la base del triangulo a calcular: ")) 
altura = int(input("Ingrese la altura del triangulo a calcular: ")) 

calcular_area(base,altura)