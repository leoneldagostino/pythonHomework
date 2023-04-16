'''
Consignas:
    Un gimnasio desea llevar el control de sus miembros. Cada miembro tiene un número de identificación, nombre, edad y tipo de membresía (por ejemplo, mensual o anual). La información se encuentra almacenada en una lista de listas, donde cada sublista representa a un miembro y contiene los siguientes elementos: número de identificación, nombre, edad y tipo de membresía.

    Escriba un programa que permita a los usuarios realizar las siguientes operaciones:

    Agregar un nuevo miembro: el programa debe pedir al usuario que ingrese el número de identificación, nombre, edad y tipo de membresía del nuevo miembro. La información debe ser agregada a la lista de diccionarios.
    
    
    Mostrar toda la información de todos los miembros (número de identificación, nombre, edad y tipo de membresía).
    
    Actualizar el tipo de membresía de un miembro: el programa debe pedir al usuario que ingrese el número de identificación del miembro y el nuevo tipo de membresía. El programa debe buscar el miembro en la lista de diccionario y actualizar el tipo de membresía correspondiente.
    
    Buscar información de un miembro: el programa debe pedir al usuario que ingrese el número de identificación del miembro. El programa debe buscar el miembro en la lista de diccionarios y mostrar su nombre, edad y tipo de membresía.
    
    Calcular el promedio de edad de los miembros: el programa debe recorrer la lista de diccionarios y calcular el promedio de edad de los miembros.
    
    Buscar el miembro más joven y el más viejo: el programa debe buscar la edad máxima y mínima en la lista de diccionarios y mostrar el nombre y número de identificación correspondientes.

'''


#Leonel D'agostino 1H


lista_miembros =\
[
    {
        "id":213,
        "nombre":"mariano",
        "edad":32,
        "membresia":"anual"   
    },
    {
        "id":76,
        "nombre":"leonel",
        "edad":22,
        "membresia":"mensual"   
    },
    {
        "id":53,
        "nombre":"juan",
        "edad":39,
        "membresia":"anual"   
    },
    {
        "id":132,
        "nombre":"esteban",
        "edad":28,
        "membresia":"mensual"   
    }
]

while True:
    # Mostrar menú de opciones
    print("Menú de opciones: \n" 
          "1. Agregar un nuevo miembro\n" 
          "2. Mostrar la informacion de todos los miembros\n"
          "3. Actualizar el tipo de membresía de un miembro\n"
          "4. Buscar información de un miembro\n"
          "5. Calcular el promedio de edad de los miembros\n"
          "6. Buscar el miembro más joven y el más viejo\n"
          "0. Salir del programa\n")
    opcion = int(input("\nIngrese la opción deseada: "))
    
    match opcion:
    #Agregar un nuevo miembro
        case 1:
            id_nuevo = int(input("Ingrese id del nuevo miembro: "))
            lista_id = []
            #validamos que no exista id identico    
            for indice in lista_miembros:
                lista_id.append(indice["id"])
            while id_nuevo in lista_id:
                id_nuevo = int(input("ID ya existe. Ingrese otro id para el miembro: "))
                
            
            
            nombre_nuevo = input("Ingrese el nombre del nuevo miembro: ")
            edad_nuevo = int(input("Ingrese edad del nuevo miembro: "))
            
            membresia_nuevo = int(input("Ingrese el tipo de membresia(1=Anual - 2=Mensual): "))
            while True:
                if membresia_nuevo == 1:
                    membresia_nuevo = "Anual"
                    break
                elif membresia_nuevo == 2:
                    membresia_nuevo = "Mensual"
                    break
                else:
                    print("Error. Ingrese una opcion valida")
                    membresia_nuevo = int(input("Ingrese el nro de su membresia (1=anual - 2=mensual): "))
            
            #creamos el diccionario del usuario
            usuario_nuevo = {'id':id_nuevo,'nombre':nombre_nuevo,'edad':edad_nuevo,'membresia':membresia_nuevo}
            
            
            #agregamos a la lista
            lista_miembros.append(usuario_nuevo)
            
            print("\nUsuario ingresado")
            print('-'*75)
            
        case 2:
            #imprimimos a los miembros
            for i in lista_miembros:
                print("Id: {} - Nombre: {} - Edad: {} - Membresia: {}".format(i["id"],i["nombre"],i["edad"],i["membresia"]))
            print('-'*75)
        #modificacion de membresia por id  
        case 3:
            id_cambio = int(input("Ingrese el id del miembro a modificar: "))
            lista_id = []
            indice_modificar = -1
            
            for indice in lista_miembros:
                lista_id.append(indice["id"])
            #validamos que el id exista   
            while not id_cambio in lista_id:
                id_cambio = int(input("Este ID no exite.\nIngrese el id del miembro a modificar: "))
            for indice in range(len(lista_id)):
                if id_cambio == lista_id[indice]:
                    indice_modificar = indice
                    break
            usuario_encontrado = lista_miembros[indice_modificar]
            print("Usuario encontrado: \n"
                  "ID: {} - Nombre: {} - Edad: {} - Membresia: {} ".format(usuario_encontrado['id'],usuario_encontrado['nombre'],usuario_encontrado['edad'],usuario_encontrado['membresia']))
            
            if indice_modificar != -1:
                membresia_nueva = int(input("Ingrese el tipo de membresia nueva para {} (1=Anual - 2=Mensual): ".format(usuario_encontrado["nombre"])))
            #validamos que ingrese la opcion correcta
                while True:
                    if membresia_nueva == 1:
                        lista_miembros[indice_modificar]["membresia"] = "Anual"
                        print("\nUsuario actualizado\n")
                        break
                    elif membresia_nueva == 2:
                        lista_miembros[indice_modificar]["membresia"] = "Mensual"
                        print("\nUsuario actualizado\n")
                        break
                    else:
                        membresia_nueva = int(input("Valor invalido.\n Ingrese el tipo de membresia nueva para {0} (1=anual - 2=mensual): ".format(usuario_encontrado['id'],usuario_encontrado['nombre'],usuario_encontrado['edad'],usuario_encontrado['membresia'])))
            
            for i in lista_miembros:
                print("Id: {} - Nombre: {} - Edad: {} - Membresia: {}".format(i["id"],i["nombre"],i["edad"],i["membresia"]))
            print('-'*75)  
        #Buscar informacion de un miembro 
        case 4:
            buscar_miembro = int(input("Ingrese el id del miembro que busca: "))
            indice_buscador = -1
            lista_id = []
            
            for indice in lista_miembros:
                lista_id.append(indice["id"])
            while not buscar_miembro in lista_id:
                buscar_miembro = int(input("Este ID no exite.\nIngrese el id del miembro a modificar: "))
            
                
            for indice in range(len(lista_id)):
                if buscar_miembro == lista_id[indice]:
                    indice_buscador = indice   
                    break
            usuario_encontrado = lista_miembros[indice_buscador]
            print("\nUsuario encontrado: \n"
                  "ID: {} - Nombre: {} - Edad: {} - Membresia: {} ".format(usuario_encontrado['id'],usuario_encontrado['nombre'],usuario_encontrado['edad'],usuario_encontrado['membresia']))
            
            print('-'*75)
        #Buscar el promedio de edades
        case 5:
            
            lista_edad = []
            for indice in lista_miembros:
                lista_edad.append(indice['edad'])
            promedio_edad = sum(lista_edad) / len(lista_edad)
            #imprimo el promedio
            print("El promedio de edad es: {}\n".format(promedio_edad))
            
            print("-"*75,"\n")
        #buscar el mimebro mas joven y el mas viejo
        case 6:
            lista_id = []
            lista_edad = []
            for indice in lista_miembros:
                lista_id.append(indice["id"])
                lista_edad.append(indice['edad'])
            
            edad_maxima = lista_edad[0]
            edad_minima = lista_edad[0]
            lista_edad_maxima = []
            lista_edad_minima = []
            
            #busco la edad max y min
            for i in range(len(lista_id)):
                if lista_edad[i] > edad_maxima:
                    edad_maxima = lista_edad[i]

                if lista_edad[i] < edad_minima:
                    edad_minima = lista_edad[i]
                    
            for i in lista_edad:
                if i == edad_maxima:
                    lista_edad_maxima.append(i) 

            for i in lista_edad:
                if i == edad_minima:
                    lista_edad_minima.append(i)
                    
            
            #Muestro edad maximas
            if len(lista_edad_maxima) == 1:
                for i in range(len(lista_id)):
                    if edad_maxima == lista_edad[i]:
                        print("\nEl miembro mayor es: \n {0} con {1} ".format(lista_miembros[i]['nombre'],lista_miembros[i]['edad']))
            else:
                print("\nLos miembros con mayor edad son: \n")
                for i in range(len(lista_id)):
                    if edad_maxima == lista_edad[i]:
                        print("{0} con {1} años ".format(lista_miembros[i]['nombre'],lista_miembros[i]['edad']))
                        
            #Muestro edad minimas
            if len(lista_edad_minima) == 1:
                for i in range(len(lista_id)):
                    if edad_minima == lista_edad[i]:
                        print("\nEl miembro mas joven:\n {0} con {1} ".format(lista_miembros[i]['nombre'],lista_miembros[i]['edad']))
            else:
                print("\nLos miembros con menor edad son: \n")
                for i in range(len(lista_id)):
                    if edad_minima == lista_edad[i]:
                        print("{0} con {1} años ".format(lista_miembros[i]['nombre'],lista_miembros[i]['edad']))
                        
                    
            print("-"*75,"\n")

            
        case 0:
            print("Salir")
            break
        case other:
            print("Opcion no valida\n")
        
   