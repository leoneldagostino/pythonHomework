# Ingresar la edad y imprimir segun la edad si es adulto, adolescente o menor de edad
#<  >


edad = int(input("Ingrese su edad: "))

if edad > 13 and edad <= 17:
    print("Eres un adolescente") 
elif edad > 17:
    print("Eres un adulto")
else:
    print("Eres menor de edad")
