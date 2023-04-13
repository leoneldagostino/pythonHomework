#leonel D'agostino 1° H


lista_id = [21,42,53,80]
lista_nombres = ["Mariano","Juan","Esteban","Mariela"]
lista_edad = [25,85,25,85]
lista_membresias = ["anual","mensual","anual","mensual"]
edad_maxima = lista_edad[0] 
edad_minima = lista_edad[0] 
lista_edad_maximas = []
lista_edad_minimas = []


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
            
            
            id_nuevo = int(input("ingrese su Id: "))
            while id_nuevo in lista_id:
                id_nuevo = int(input("ERROR. El id ingresado ya existe, ingrese otro id: "))
            lista_id.append(id_nuevo)
                
            nombre_nuevo = input("ingrese su nombre: ")
            lista_nombres.append(nombre_nuevo)
                
            edad_nuevo = int(input("ingrese su edad: "))
            lista_edad.append(edad_nuevo)
            
            
            membresia_nuevo = int(input("ingrese el nro de su membresia: *valor numerico* (1 anual - 2 mensual)"))
            while True:
                if membresia_nuevo == 1:
                    lista_membresias.append("Anual")
                    break
                
                elif  membresia_nuevo == 2:  
                    lista_membresias.append("Mensual")
                    break
                else:
                    print("Error ingrese una opcion valida")
                lista_membresias.append(membresia_nuevo)
                    

    
    #Agregar un msotrar la informacion de todos los miembros
        case 2:
            for i in range(len(lista_id)):
                print("{0} - {1} - {2} - {3}".format(lista_id[i],lista_nombres[i],lista_edad[i],lista_membresias[i]))

    #Actualizar el tipo de membresia de un miembro
        case 3:
            id_miembro = int(input("Ingrese el id del miembro nuevo: "))
            indice_id_modificar = -1

            for i in range(len(lista_id)):
      
                if id_miembro == lista_id[i]:
                    indice_id_modificar = i
                break

            print("{0} - {1} - {2} - {3}".format(lista_id[indice_id_modificar],lista_nombres[indice_id_modificar],lista_edad[indice_id_modificar],lista_membresias[indice_id_modificar]))
   
            if indice_id_modificar != -1:
                
                membresia_nueva = input("Ingrese el tipo de membresia nueva para {0}".format(lista_nombres[indice_id_modificar]))
                lista_membresias[indice_id_modificar] = membresia_nueva
            else:
                print("Ese id no existe en la lista, ingrese uno nuevo")
            
            print("\n\n")


            for i in range(len(lista_id)):
                print("{0} - {1} - {2} - {3}".format(lista_id[i],lista_nombres[i],lista_edad[i],lista_membresias[i]))
    #Buscar informacion de un miembro
        case 4:
            id_miembro = int(input("Ingrese el id del miembro: "))
            indice_id_modificar = -1

            for i in range(len(lista_id)):
            
                if id_miembro == lista_id[i]:
                    indice_id_modificar = i
                break

            print("{0} - {1} - {2} - {3}".format(lista_id[indice_id_modificar],lista_nombres[indice_id_modificar],lista_edad[indice_id_modificar],lista_membresias[indice_id_modificar]))    
            
    #Calcular el promedio de edad e los miembros
        case 5:
            
            promedio_edad = sum(lista_edad) / len(lista_edad)
            print("El promedio de edad es:", promedio_edad)
            
    #Buscar el miembro mas joven y el mas viejo
        case 6:
            for i in range(len(lista_id)):
                print("{0} - {1} - {2} - {3}".format(lista_id[i],lista_nombres[i],lista_membresias[i],lista_edad[i]))

            edad_maxima = lista_edad[0] 
            edad_minima = lista_edad[0]

            #Busco la edad minima y maxima
            for i in range(len(lista_id)):
                if lista_edad[i] > edad_maxima:
                    edad_maxima = lista_edad[i]
                    lista_edad_maximas.append(lista_edad) 

                if lista_edad[i] < edad_minima:
                    edad_minima = lista_edad[i]

            #Muestro edad maximas
            for i in range(len(lista_id)):
                if edad_maxima == lista_edad[i]:
                    if len(lista_edad_maximas) < 1:
                        print("El miembro mayor es: \n {0} con {1} ".format(lista_nombres[i],lista_edad[i]))
                    else:
                        print("Los miembros con mayor edad son: ")
                        print("{0} con {1} años ".format(lista_nombres[i],lista_edad[i]))
                    
                        
                        
                  

            for i in range(len(lista_id)):
                if edad_minima == lista_edad[i]:
                    if len(lista_edad_minimas) < 1:
                        print("{0} - {1} ".format(lista_nombres[i],lista_edad[i]))
                    else:
                        print("Los miembros con menor edad son: ")
                        print("{0} con {1} años ".format(lista_nombres[i],lista_edad[i]))
                        
            
            # for i in lista_edad_maximas:
            #     print("El miembro mayor es: {0} con {1} años ".format(lista_nombres[i],lista_edad[i]))

            #     print("\n")

            # for i in lista_edad_minimas:
            #     if lista_edad_minimas == 1:
            #         print("El miembro mas joven es: {0} con {1} años".format(lista_nombres[i],lista_edad[i]))
            #     else:
            #         print("Los miembros mas jovenes son:")
            #         print("{0} con {1} años".format(lista_nombres[i],lista_edad[i]))
                    

        case 0:
            print("salir")
            break
        case other:
            print("Opcion no valida")
        
        

