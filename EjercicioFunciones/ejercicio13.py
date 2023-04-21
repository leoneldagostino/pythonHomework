'''

13.
Crear una función que recibe una lista de palabras y devuelve un diccionario con las palabras como llaves y su longitud como valores.

'''

def lista_a_diccionario(lista):
    diccionario_palabras = {}
    
    for elemento in lista:
        longitud = len(elemento)
        diccionario_palabras.update({elemento : longitud})
        
    return diccionario_palabras

lista = ["pedro","diego","leo","fede","jorge"]

print(lista_a_diccionario(lista))