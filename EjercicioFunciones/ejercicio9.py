'''
9.

Crear una función que cuente la cantidad de veces que aparece un elemento en una lista. 
Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.

'''

def contador_elemento(lista,elemento_buscar):
    contador_elemento = 0
    for elemento in lista:
        if elemento == elemento_buscar:
            contador_elemento += 1
    
    return contador_elemento

lista_x = ["hola","hola","fede","diego","diego","diego"]

print(contador_elemento(lista_x,"diego"))