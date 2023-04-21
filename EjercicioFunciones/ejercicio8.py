'''
Crear una función que verifique si un número es par o impar.
Recibe un número como parámetro y devuelve True si es par o False si es impar

'''

def calcular_par_impar(numero):
    
    if numero % 2 == 0:
        return True
    else:
        return False


numero = int(input("Ingrese el numero para saber si es par o impar: "))
calcular_par_impar(numero)

if numero == True:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")