'''
Crear una función llamada es_entero que reciba un string y devuelva True en caso de que se trate de un número entero y False en caso contrario.
'''
import re

def es_entero(texto:str):
    retorno = re.findall(r'([a-zA-Z ]+)',texto)
    
    if retorno == []:
        retorno = re.findall(r'([0-9 ]+)',texto)
        if retorno[0].isdigit():
            return True
    else:
        return False
            
        
        
prueba = '213123'

print(es_entero(prueba))