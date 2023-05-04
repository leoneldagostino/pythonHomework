'''
Crear una función llamada es_minuscula que reciba un string y devuelva True en caso de que todas las letras sean mayúsculas o False en el caso contrario
'''
import re

def es_minuscula(texto:str):
    retorno = re.findall(r'([A-Z ]+)',texto)
    
    for letras in retorno:
        #recorremos la lista para poder evaluar los textos 
        if letras.isupper():
            return False
        else:
            return True
        
prueba = 'ASDDffDASs ASss'
prueba2 = 'aaaa aaaa'

print(es_minuscula(prueba))#False
print(es_minuscula(prueba2))#True