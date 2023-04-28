from data_stark import lista_personajes
'''

Consigna:

    Analizar detenidamente el set de datos
    Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
    Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
    Calcular e informar cual es el superhéroe más y menos pesado.
    Ordenar el código implementando una función para cada uno de los valores informados.
    Construir un menú que permita elegir qué dato obtener

'''
'''

Leonel D'agostino 1-H
'''

def espacio():
    print('-'*75)

def imprimir_hereos():
    print("El nombre del superheroe: ",end="\n")
    for indice in lista_personajes:
        print(" {} \n".format(indice["nombre"]))
    
    espacio()
    
def imprimir_hereos_altura():
    print("El nombre del superheroe y su altura:",end="\n")
    for indice in lista_personajes:
        print("Nombre{0} altura: {1} cm \n".format(indice["nombre"],indice["altura"]))
    espacio()
    
def imprimir_hereo_mas_alto():
    print("El superhereo mas alto es: ",end='\n')
    hereo_mas_alto = float(lista_personajes[0]['altura'])
    indice_heroe_mas_alto = lista_personajes[0]

    #buscamos el mas alto
    for indice in lista_personajes:
        altura = float(indice["altura"])
        if altura > hereo_mas_alto:
            indice_heroe_mas_alto = indice
            hereo_mas_alto = altura


    #imprimimos el nombre y altura del hereo mas alto
    print("El mas alto es: {} - {} \n".format(indice_heroe_mas_alto['nombre'],hereo_mas_alto))
    espacio()
    
def imprimir_hereo_mas_bajo():
    print("El superhereo mas bajo es: ",end='\n')
    hereo_mas_bajo = float(lista_personajes[0]['altura'])
    indice_heroe_mas_bajo = lista_personajes[0]

    #buscamos el mas alto
    for indice in lista_personajes:
        altura = float(indice["altura"])
        if altura < hereo_mas_bajo:
            indice_heroe_mas_bajo = indice
            hereo_mas_bajo = altura


    #imprimimos el nombre y altura del hereo mas bajo
    print("El mas bajo es: {} - {} \n".format(indice_heroe_mas_bajo['nombre'],hereo_mas_bajo))
    espacio()
    
def imprimir_promedio_altura():
    altura_total_hereos = 0
    numero_hereos= len(lista_personajes)
    for indice in lista_personajes:
        altura = float(indice["altura"])
        altura_total_hereos += altura
        

    promedio_altura = float(altura_total_hereos / numero_hereos)
    print("El promedio de altura de los hereos es: {} \n".format(promedio_altura))
    espacio()
    
def imprimir_identidad():
    for indice in lista_personajes:
        print("Identidad: {} - Nombre hereo: {} - altura: {}  \n".format(indice['identidad'],indice["nombre"],indice["altura"]))
    print('\n')
    espacio()

def mostrar_hereo_pesado_liviano():
    indice_hereo_pesado = lista_personajes[0]
    indice_hereo_liviano = lista_personajes[0]

    for indice in lista_personajes:
        
        #buscamos hereo mas pesado
        peso_hereo_pesado = float(indice_hereo_pesado["peso"])
        mas_pesado = float(indice['peso'])
        if mas_pesado > peso_hereo_pesado:
            indice_hereo_pesado = indice
            
        #buscar hereo mas liviano
        peso_hereo_liviano = float(indice_hereo_liviano["peso"])
        mas_liviano = float(indice["peso"])
        if mas_liviano < peso_hereo_liviano:
            indice_hereo_liviano = indice
            
            
        #imprimos ambos hereos
    print("A continuacion los heroes mas liviano y pesado son: \n" 
            "El mas es pasado es: {0} con {1} kg \n"
            "El mas liviano es: {2} con {3} \n".format(indice_hereo_pesado['nombre'],indice_hereo_pesado["peso"],indice_hereo_liviano['nombre'],indice_hereo_liviano['peso']))
    espacio()

#Menu de opciones
while True:
    print("1.Imprimir nombre de cada superheroe\n"
          "2.Imprimir nombre de cada superheroe y la altura\n"
          "3.Imprimir el super heroe mas alto\n"
          "4.Imprimir el super heroe mas bajo\n"
          "5.Imprimir la altura promedio de los superheroes\n"
          "6.informar identidad el superhereo asociado a los indicadroes anteriores\n"
          "7.Calcular cual es el superheroe mas y menos pesado\n"
          "0.Salir\n")

    opcion = int(input("Ingrese una opcion: "))

    match opcion:
        #imprimir nombre de cada superhereo
        case 1:
            imprimir_hereos()
            
        case 2:
            imprimir_hereos_altura()
        
        #mostrar hereo mas alto
        case 3:
            imprimir_hereo_mas_alto()
        #mostrar hereo mas bajo
        case 4:
            imprimir_hereo_mas_bajo()

        #Imprimir la altura promedio de los superheroes
        case 5:
            imprimir_promedio_altura()
            
        case 6:
            imprimir_identidad()
            
        case 7:
            mostrar_hereo_pesado_liviano()
                     
        case 0:
            print("Salir")
            break
        case other:
            print("Valor invalido.")
