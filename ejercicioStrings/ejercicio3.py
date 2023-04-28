'''
Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos strings concatenados, separados por un espacio
'''

def string_concatenado(string_1:str, string_2:str):
    string_concatenado = " "
    str = string_concatenado.join([string_1,string_2])
    return str

tex1 = 'hola'
tex2 = 'mundo'
tex3 = string_concatenado(tex1,tex2)
print(tex3)