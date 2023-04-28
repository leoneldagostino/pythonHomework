'''
Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario con el nombre y apellido, eliminando los espacios del comienzo y el final y colocando la primer letra en mayúscula
'''
def string_to_diccionario(nombre:str,apellido:str):
    diccionario = {}
    nombre_para_dict = nombre.strip().capitalize()
    apellido_para_dict = apellido.strip().capitalize()
    
    diccionario["Nombre"] = nombre_para_dict
    diccionario["Apellido"] = apellido_para_dict
    
    return diccionario

print(string_to_diccionario("leonel       ","          d'agostino"))