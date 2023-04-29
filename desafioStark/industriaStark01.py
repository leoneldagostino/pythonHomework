from data_stark import lista_personajes


def imprimir_lista(lista):
    for elemento in lista:
        print("El hereo: {} - genero: {}".format(elemento["nombre"],elemento["genero"]))
    
                
def retornar_lista_por_genero(lista:list,genero:str):
    '''
    Returna una lista filtrada por genero recibiendo la lista a filtrar como parametro
    '''
    lista_genero = []
    for elemento in lista:
        if genero == elemento["genero"]:
            lista_genero.append(elemento)
    return lista_genero

lista_hereo_masculinos = retornar_lista_por_genero(lista_personajes,"M")
imprimir_lista(lista_hereo_masculinos)
lista_hereo_femenino = retornar_lista_por_genero(lista_personajes,"F")
imprimir_lista(lista_hereo_femenino)


def imprimir_hereo_mas_alto(lista:list):
    hereo_mas_alto = float(lista[0]['altura'])
    indice_heroe_mas_alto = lista[0]

    
    #buscamos el mas alto
    for heroe in lista:
        altura = float(heroe["altura"])
        if altura > hereo_mas_alto:
            indice_heroe_mas_alto = heroe
            hereo_mas_alto = altura


    #imprimimos el nombre y altura del hereo mas alto
    return "El mas alto es: {} - {} \n".format(indice_heroe_mas_alto['identidad'],hereo_mas_alto)



def imprimir_hereo_mas_bajo(lista:list):

    hereo_mas_bajo = float(lista[0]['altura'])
    indice_heroe_mas_bajo = lista[0]
    #buscamos el mas bajo
    for heroe in lista:            
        altura = float(heroe["altura"])
        if altura < hereo_mas_bajo:
            indice_heroe_mas_bajo = heroe
            hereo_mas_bajo = altura


    #imprimimos el nombre y altura del hereo mas bajo
    return "El mas bajo es: {} - {} \n".format(indice_heroe_mas_bajo['identidad'],hereo_mas_bajo)


def imprimir_promedio_altura(lista:list):
    altura_total_hereos = 0
    numero_hereos= len(lista)
    for hereo in lista:
        altura = float(hereo["altura"])
        altura_total_hereos += altura
        

    promedio_altura = float(altura_total_hereos / numero_hereos)
    return"El promedio de altura de los heroes es: {} \n".format(promedio_altura)
        


def contador_hereos_color_ojos(lista:list):
    tipos_color_ojos = {}
    for heroe in lista:
        if heroe["color_ojos"] not in tipos_color_ojos:
            tipos_color_ojos.update({heroe["color_ojos"]:1})
        else:
            tipos_color_ojos[heroe["color_ojos"]] += 1
    return tipos_color_ojos


def contador_hereos_color_pelo(lista:list):
    tipos_color_pelo = {}
    for heroe in lista:
        if heroe["color_pelo"] not in tipos_color_pelo:
            if heroe["color_pelo"] == "":
                continue
            tipos_color_pelo.update({heroe["color_pelo"]:1})
        else:
            tipos_color_pelo[heroe["color_pelo"]] += 1
    return tipos_color_pelo
 

def contador_tipo_inteligencia(lista:list):
    tipos_inteligencia = {}
    for heroe in lista:
        if heroe["inteligencia"] not in tipos_inteligencia:
            if heroe["inteligencia"] == "":
                tipos_inteligencia.update({"No tiene":1})
                continue
            tipos_inteligencia.update({heroe["inteligencia"]:1})
        else:
            tipos_inteligencia[heroe["inteligencia"]] += 1
    return tipos_inteligencia
        

def agrupador_color_ojos(lista:list):
    agrupacion_heroe_por_color_ojos = {}
    for heroe in lista:
        if heroe["color_ojos"] not in agrupacion_heroe_por_color_ojos:
            agrupacion_heroe_por_color_ojos.update({heroe["color_ojos"]:[heroe["nombre"]]})
        else:
            corregimos_lista = agrupacion_heroe_por_color_ojos[heroe["color_ojos"]] 
            corregimos_lista.append(heroe["nombre"])
            agrupacion_heroe_por_color_ojos[heroe["color_ojos"]] = corregimos_lista
    return agrupacion_heroe_por_color_ojos
    
def agrupador_color_pelo(lista:list):
    agrupacion_heroe_por_color_pelo = {}
    for heroe in lista:
        if heroe["color_pelo"] not in agrupacion_heroe_por_color_pelo:
            if heroe["color_pelo"] == "":
                continue
            agrupacion_heroe_por_color_pelo.update({heroe["color_pelo"]:[heroe["nombre"]]})
        else:
            corregimos_lista = agrupacion_heroe_por_color_pelo[heroe["color_pelo"]] 
            corregimos_lista.append(heroe["nombre"])
            agrupacion_heroe_por_color_pelo[heroe["color_pelo"]] = corregimos_lista
    return agrupacion_heroe_por_color_pelo
        
def agrupador_inteligencia(lista:list):
    agrupacion_heroe_por_inteligencia = {}
    for heroe in lista:
        if heroe["inteligencia"] not in agrupacion_heroe_por_inteligencia:
            if heroe["inteligencia"] == "":
                agrupacion_heroe_por_inteligencia.update({"No tiene":[heroe["nombre"]]})
                continue
            agrupacion_heroe_por_inteligencia.update({heroe["inteligencia"]:[heroe["nombre"]]})
        else:
            corregimos_lista = agrupacion_heroe_por_inteligencia[heroe["inteligencia"]] 
            corregimos_lista.append(heroe["nombre"])
            agrupacion_heroe_por_inteligencia[heroe["inteligencia"]] = corregimos_lista
    return agrupacion_heroe_por_inteligencia







