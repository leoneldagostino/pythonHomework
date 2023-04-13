#Ingresar un nombre, si es juan,maria o pedro diga "Hola [nombre]", sino "Hola desconocido"

nombre = input("Ingrese su nombre: ")

if nombre == "juan":
    print("Hola {}".format(nombre))
elif nombre == "maria":
    print("Hola {}".format(nombre))
elif nombre == "pedro":
    print("Hola {}".format(nombre))
else:
    print("Hola desconocido")