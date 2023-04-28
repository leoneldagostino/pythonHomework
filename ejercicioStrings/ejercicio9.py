'''
Escribir una función que tome una lista de nombres y los una en una sola cadena separada por un salto de línea, por ejemplo: ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".
'''

def lista_to_string(lista):
    cadena = ""
    for palabra in lista:
        cadena += palabra + "\n"
    
    return cadena
        
lista_nombres = ["Juan","Maria","Pedro"]

print(lista_to_string(lista_nombres))
        