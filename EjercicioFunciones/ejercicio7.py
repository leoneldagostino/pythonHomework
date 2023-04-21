'''
Crear una función que calcule el máximo común divisor de dos números. 
Recibe dos parámetros (números) y devuelve el máximo común divisor.

'''

def mcd(numero1,numero2):
    lista_divisores1 = []
    lista_divisores2 = []
    divisores_comunes = []
    for numero in range (1,numero1):
        if numero1 % numero == 0:
            lista_divisores1.append(numero)
        
    for numero in range (1,numero2):
        if numero2 % numero == 0:
            lista_divisores2.append(numero)
            
    for numeros in lista_divisores1:
        divisor = numeros
        for numeros2 in lista_divisores2:
            divisor2 = numeros2
            if divisor == divisor2:
                divisores_comunes.append(divisor)
                
    return divisores_comunes[-1]


print(mcd(18,24))
                
        
        