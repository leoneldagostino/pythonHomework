'''
Escribir una función que tome un string y un carácter y devuelva el número de veces que aparece ese carácter en el string.
'''

def caracteres_buscar_apariciones(string:str,caractaer_buscar:str):
    cantidad_apariciones = string.count(caractaer_buscar)
    return cantidad_apariciones

texto = "Hola juan carlos carlos"

print(caracteres_buscar_apariciones(texto,"los"))