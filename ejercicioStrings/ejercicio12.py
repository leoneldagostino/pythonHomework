'''
Escribir una función que tome un número de tarjeta de crédito como input,
verificar que todos los caracteres sean numéricos y devolver los últimos cuatro dígitos
y los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234"
'''

def verificar_tarjeta_credito(credit_numeros):
    
    numeros = credit_numeros.replace(" ","")
    verificacion = numeros.isdigit()
    
    if verificacion:
        return numeros[-4:]
    else:
        return f'No es una tarjeta de credito valida'
    
    
tarjet = input("Ingrese numero de tarjeta: ")
print(verificar_tarjeta_credito(tarjet))