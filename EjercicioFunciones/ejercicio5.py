'''
5.
Crear una función que determine si un número es primo o no. 
Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.

'''

def determinar_primo(numero):
    
    es_primo = True
    for num in range(2,numero):
        
        if numero % num == 0:
            print("No es primo, {} es divisor".format(num))
            es_primo = False

    if es_primo:
        print("El numero es primo")
        
numero = int(input("Ingrese el numero: "))

determinar_primo(numero)