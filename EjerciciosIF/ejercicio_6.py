#programa que reciba nombre y edad
#determinar si puede votar o no, si es mayor a 18 y menor de 65

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad <= 65 and edad >= 18:
    print("Puedes votar")
else: 
    print("No puede votar")