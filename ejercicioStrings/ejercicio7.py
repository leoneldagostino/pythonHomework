'''
Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados
'''
def eliminar_espacios_string(string:str):
    string_espacio_eliminados = string.strip()
    return string_espacio_eliminados

texto = "     Este es mi texto            "
texto_sin_espacio = eliminar_espacios_string(texto)
print(texto_sin_espacio)
