from data_stark import lista_personajes


def imprimir_heroe_genero(lista,genero:str):
    for heroe in lista:
        if genero == heroe["genero"]:
            print("El hereo: {}".format(heroe["nombre"]))
    
                
        
# imprimir_hereo_genero(lista_personajes,"M")
# imprimir_hereo_genero(lista_personajes,"F")

def imprimir_hereo_mas_alto(genero:str):
    print("El superhereo mas alto es: ",end='\n')
    hereo_mas_alto = float(lista_personajes[0]['altura'])
    indice_heroe_mas_alto = lista_personajes[0]

    
    #buscamos el mas alto
    for heroe in lista_personajes:
        if genero == heroe["genero"]:
            altura = float(heroe["altura"])
            if altura > hereo_mas_alto:
                indice_heroe_mas_alto = heroe
                hereo_mas_alto = altura


    #imprimimos el nombre y altura del hereo mas alto
    return "El mas alto es: {} - {} \n".format(indice_heroe_mas_alto['identidad'],hereo_mas_alto)


# imprimir_hereo_mas_alto("F")
# imprimir_hereo_mas_alto("M")

def imprimir_hereo_mas_bajo(genero:str):
    print("El superhereo mas bajo es: ",end='\n')
    lista_heroes = []

    for heroe in lista_personajes:
        if genero == heroe["genero"]:
            lista_heroes.append(heroe)
    hereo_mas_bajo = float(lista_heroes[0]['altura'])
    indice_heroe_mas_bajo = lista_heroes[0]
    #buscamos el mas bajo
    for heroe in lista_heroes:            
        altura = float(heroe["altura"])
        if altura < hereo_mas_bajo:
            indice_heroe_mas_bajo = heroe
            hereo_mas_bajo = altura


    #imprimimos el nombre y altura del hereo mas bajo
    if genero == "F":
        return "El mas bajo femenino es: {} - {} \n".format(indice_heroe_mas_bajo['identidad'],hereo_mas_bajo)
    elif genero == "M":
        return "El mas bajo masculino es: {} - {} \n".format(indice_heroe_mas_bajo['identidad'],hereo_mas_bajo)


# imprimir_hereo_mas_bajo("F")
# imprimir_hereo_mas_bajo("M")

def imprimir_promedio_altura(genero:str):
    lista_hereos = []
    for hereo in lista_personajes:
        if hereo["genero"] == genero:
            lista_hereos.append(hereo)
            
    altura_total_hereos = 0
    numero_hereos= len(lista_hereos)
    for hereo in lista_hereos:
        altura = float(hereo["altura"])
        altura_total_hereos += altura
        

    promedio_altura = float(altura_total_hereos / numero_hereos)
    if genero == "F":
        return"El promedio de altura de los hereo femeninos es: {} \n".format(promedio_altura)
    else:
        return "El promedio de altura de los hereos masculino es: {} \n".format(promedio_altura)
        

# imprimir_promedio_altura("F")
# imprimir_promedio_altura("M")


def contador_hereos_color_ojos():
    tipos_color_ojos = {}
    for heroe in lista_personajes:
        if heroe["color_ojos"] not in tipos_color_ojos:
            tipos_color_ojos.update({heroe["color_ojos"]:1})
        else:
            tipos_color_ojos[heroe["color_ojos"]] += 1
    for tipo,valor in tipos_color_ojos.items():
        print("{}: {}".format(tipo,valor))

contador_hereos_color_ojos()                    
#contador_hereos_color_ojos()

def contador_hereos_color_pelo():
    tipos_color_pelo = {}
    for heroe in lista_personajes:
        if heroe["color_pelo"] not in tipos_color_pelo:
            if heroe["color_pelo"] == "":
                continue
            tipos_color_pelo.update({heroe["color_pelo"]:1})
        else:
            tipos_color_pelo[heroe["color_pelo"]] += 1
    for tipo,valor in tipos_color_pelo.items():
        print("{}: {}".format(tipo,valor))
 
# contador_hereos_color_pelo()

def contador_tipo_inteligencia():
    tipos_inteligencia = {}
    for heroe in lista_personajes:
        if heroe["inteligencia"] not in tipos_inteligencia:
            if heroe["inteligencia"] == "":
                tipos_inteligencia.update({"No tiene":1})
                continue
            tipos_inteligencia.update({heroe["inteligencia"]:1})
        else:
            tipos_inteligencia[heroe["inteligencia"]] += 1
    for tipo,valor in tipos_inteligencia.items():
        print("{}: {}".format(tipo,valor))
        
# contador_tipo_inteligencia()

def agrupador_color_ojos():
    agrupacion_heroe_por_color_ojos = {}
    for heroe in lista_personajes:
        if heroe["color_ojos"] not in agrupacion_heroe_por_color_ojos:
            agrupacion_heroe_por_color_ojos.update({heroe["color_ojos"]:[heroe["nombre"]]})
        else:
            corregimos_lista = agrupacion_heroe_por_color_ojos[heroe["color_ojos"]] 
            corregimos_lista.append(heroe["nombre"])
            agrupacion_heroe_por_color_ojos[heroe["color_ojos"]] = corregimos_lista
    for tipo,valor in agrupacion_heroe_por_color_ojos.items():
        print("{}: {}".format(tipo,valor))

    
def agrupador_color_pelo():
    agrupacion_heroe_por_color_pelo = {}
    for heroe in lista_personajes:
        if heroe["color_pelo"] not in agrupacion_heroe_por_color_pelo:
            if heroe["color_pelo"] == "":
                continue
            agrupacion_heroe_por_color_pelo.update({heroe["color_pelo"]:[heroe["nombre"]]})
        else:
            corregimos_lista = agrupacion_heroe_por_color_pelo[heroe["color_pelo"]] 
            corregimos_lista.append(heroe["nombre"])
            agrupacion_heroe_por_color_pelo[heroe["color_pelo"]] = corregimos_lista
    for tipo,valor in agrupacion_heroe_por_color_pelo.items():
        print("{}: {}".format(tipo,valor))
        
def agrupador_inteligencia():
    agrupacion_heroe_por_inteligencia = {}
    for heroe in lista_personajes:
        if heroe["inteligencia"] not in agrupacion_heroe_por_inteligencia:
            if heroe["inteligencia"] == "":
                agrupacion_heroe_por_inteligencia.update({"No tiene":[heroe["nombre"]]})
                continue
            agrupacion_heroe_por_inteligencia.update({heroe["inteligencia"]:[heroe["nombre"]]})
        else:
            corregimos_lista = agrupacion_heroe_por_inteligencia[heroe["inteligencia"]] 
            corregimos_lista.append(heroe["nombre"])
            agrupacion_heroe_por_inteligencia[heroe["inteligencia"]] = corregimos_lista
    for tipo,valor in agrupacion_heroe_por_inteligencia.items():
        print("{}: {}".format(tipo,valor))

# agrupador_inteligencia()






