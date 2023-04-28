'''
Escribir una función que tome una lista de palabras y devuelva un string que contenga todas las palabras concatenadas con comas y "y" antes de la última palabra. Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], el string resultante debería ser "manzanas, naranjas y bananas"..
'''

def lista_to_string(lista:list):
    cadena = ""
    for palabra in lista:
        if palabra is lista[-1]:
            cadena += "y "+palabra
        else:
            cadena += palabra + ","
    
    return cadena


lista_frutas = ["manzanas", "naranjas", "bananas"]

print(lista_to_string(lista_frutas))