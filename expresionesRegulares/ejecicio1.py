'''
Crear una función llamada es_mayuscula que reciba un string y devuelva True en caso de que todas las letras sean mayúsculas o False en el caso contrario
'''
import re

def es_mayuscula(texto:str):
    retorno = re.findall(r'([a-z ]+)',texto)
    
    for letras in retorno:
        #recorremos la lista para poder evaluar los textos 
        if letras.islower():
            return False
        else:
            return True
        
prueba = 'ASDDffDASs  Sas'
prueba2 = 'AAAAAAAAAAAAA  AAAAA'

print(es_mayuscula(prueba))#FALSE
print(es_mayuscula(prueba2))#TRUE
        