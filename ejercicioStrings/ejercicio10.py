'''
Escribir una función que tome un nombre y un apellido y devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar".
'''

def nombre_apellido_to_mail(nombre:str,apellido:str):
    caracteres_especiales = ("'")
    nombre = nombre.strip().lower().replace(caracteres_especiales,"")
    apellido = apellido.strip().lower().replace(caracteres_especiales,"")
    mail_utn = ""
    mail_utn = mail_utn.join([nombre,apellido,"@utn-fra.com.ar"])
    return mail_utn

print(nombre_apellido_to_mail("Leonel  ","     D'agostino"))
    