#Dada una lista de palabras, imprimir la palabra más larga de la lista.


lista_palabras = ["hola","palabra","mundo"]
palabra_mas_larga = lista_palabras[0]

for palabra in lista_palabras:
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra
        
print(palabra_mas_larga)   
