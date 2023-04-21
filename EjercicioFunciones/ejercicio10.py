'''
10.
Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.

'''

def palabra_mas_larga(lista_palabras):
    palabra_mas_larga = lista_palabras[0]

    for palabra in lista_palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
            
    return palabra_mas_larga

lista_palabras = ["palabra","mas","larga"]

print(palabra_mas_larga(lista_palabras))


