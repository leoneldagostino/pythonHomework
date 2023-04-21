'''
4.
Crear una función que calcule el promedio de edad de un grupo de personas. 
Recibe una lista de edades y devuelve el promedio.

'''

def promedio_personas(lista_personas):
    cantidad_personas = len(lista_personas)
    edades_totales = sum(lista_personas)
    promedio_edad = edades_totales / cantidad_personas
    
    print("El promedio de edades son {} ".format(promedio_edad))
    
numero_de_personas = int(input("Ingrese la cantidad de personas que son en el grupo: "))
edad_personas = []

for indice in range(0,numero_de_personas):
    edad_personas.append(int(input("Ingrese la edad de la persona: ")))

promedio_personas(edad_personas)
