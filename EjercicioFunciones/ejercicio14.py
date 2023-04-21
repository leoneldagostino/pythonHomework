'''
14.
Crear una función que recibe una lista de números y devuelve un diccionario con el valor mínimo, el valor máximo y el promedio de los números en la lista.

'''

def lista_a_diccionario(lista_numeros):
    diccionario_numeros = {}
    numero_maximo = lista_numeros[0]
    numero_minimo = lista_numeros[0]
    cantidad_numero = len(lista_numeros)
    promedio_numero =   sum(lista_numeros) / cantidad_numero
    
    diccionario_numeros.update({"promedio de los numero": promedio_numero})
    
    for numero in lista_numeros:
        if numero_maximo < numero:
            numero_maximo = numero

    for numero in lista_numeros:
        if numero_minimo > numero:
            numero_minimo = numero
            
    diccionario_numeros.update({"numero maximo": numero_maximo})
    diccionario_numeros.update({"numero minimo": numero_minimo})

    return diccionario_numeros
            
numero = [1,5,21,75,24,40,13,56]

print(lista_a_diccionario(numero))
    