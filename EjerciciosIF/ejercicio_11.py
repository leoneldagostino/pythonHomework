# Ingrese la edad del usuario y que imprima lo que correspondiente segun la edad que introduzca

edad = int(input("Ingrese su edad: "))

if edad < 64 and edad > 17:
    print("Eres un adulto")
elif edad > 12:
    print("Eres un adolescente")
else:
    print("Eres un niño")