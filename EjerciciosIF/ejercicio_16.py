#ingresar la edad y que imprima un mensaje segun corresponda su edad
# <  >
edad = int(input("Ingrese su edad: "))

if edad > 13 and edad <= 17:
    print("Eres un adolescente")
elif edad < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
    
