'''
Crear una función que calcule el descuento aplicado a un producto. 
Recibe dos parámetros (precio original y precio con descuento) y devuelve el porcentaje de descuento aplicado.

Leonel D'agostino 1H

'''

def calcular_descuento_producto(precio_original,precio_descuento):
    division = precio_original / precio_descuento
    resultado_final = 100 / division
    print ("El descuento que se le realizo al producto fue del {}%".format(resultado_final))

precio_descontado = int(input("Ingrese el precio del producto con el descuento incluido: "))
precio_sin_descuento = int(input("Ingrese el precio del producto con el precio original: "))

calcular_descuento_producto(precio_sin_descuento,precio_descontado)