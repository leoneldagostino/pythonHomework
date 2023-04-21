'''
11.
Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.

'''

def buscar_vocales(palabra):

    contador_vocales = 0
    
    for letra in palabra:
        if letra == 'a' or letra == 'A':
            contador_vocales += 1
        if letra == 'e' or letra == 'E':
            contador_vocales += 1
        if letra == 'i' or letra == 'I':
            contador_vocales += 1
        if letra == 'o' or letra == 'O':
            contador_vocales += 1
        if letra == 'u' or letra == 'U':
            contador_vocales += 1
                    
    return contador_vocales


print(buscar_vocales("palabra con vocales"))