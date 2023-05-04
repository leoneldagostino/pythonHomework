'''
Crear una función llamada es_solo_texto que reciba un string y devuelva True en caso de que trate solo de caracteres alfabéticos y el espacio y False en el caso contrario
'''
import re

def es_solo_texto(texto:str):
    retorno = re.search(r'^[a-zA-Z ]+$',texto)
    
    if retorno == None:
        return False
    else:
        return True
    
    
            
        
        
prueba = 'hola'

print(es_solo_texto(prueba))