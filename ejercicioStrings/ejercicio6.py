'''
Escribir una función que tome un string y un carácter y devuelva una lista con todas las palabras en el string que contienen ese carácter.
'''

def buscar_palabras_coincidencias(string:str,caracter_buscar:str):
    lista_palabras = []
    palabras_texto = string.split()
    
    for palabra in palabras_texto:
        if caracter_buscar in palabra:
            lista_palabras.append(palabra)
            
    return lista_palabras

texto = "este string es para el ejercicio carlos carlos carlos"

print(buscar_palabras_coincidencias(texto,"es"))
            
    
    