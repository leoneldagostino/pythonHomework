'''
Consigna:
    Escriba un programa que permita a los usuarios realizar las siguientes operaciones:

    Agregar un nuevo miembro: el programa debe pedir al usuario que ingrese el número de identificación, nombre, edad y tipo de membresía del nuevo miembro. La información debe ser agregada a las listas paralelas.


    Mostrar toda la información de todos los miembros (número de identificación, nombre, edad y tipo de membresía).

    Actualizar el tipo de membresía de un miembro: el programa debe pedir al usuario que ingrese el número de identificación del miembro y el nuevo tipo de membresía. El programa debe buscar el número de identificación en la lista de números de identificación y actualizar el tipo de membresía correspondiente en la lista de tipos de membresía. En caso de no encontrar al miembro informar con un mensaje de que el mismo no se encontró

    Buscar información de un miembro: el programa debe pedir al usuario que ingrese el número de identificación del miembro. El programa debe buscar el número de identificación en la lista de números de identificación y mostrar el nombre, edad y tipo de membresía correspondientes en las listas de nombres, edades y tipos de membresía.


    Calcular el promedio de edad de los miembros: el programa debe recorrer la lista de edades y calcular el promedio de edad de los miembros.

    Buscar el miembro más joven y el más viejo: el programa debe buscar la edad máxima y mínima en la lista de edades y mostrar el nombre y número de identificación correspondientes en las listas de nombres y números de identificación.

'''


#leonel D'agostino 1° H

lista_id = [21,42,53,80]
lista_nombres = ["Mariano","Juan","Esteban","Mariela"]
lista_edad = [25,35,25,85]
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
            id_nuevo = int(input("Ingrese su Id: "))
            while id_nuevo in lista_id:
                id_nuevo = int(input("ERROR. El id ingresado ya existe, ingrese otro id: "))
            lista_id.append(id_nuevo)
                
            nombre_nuevo = input("Ingrese su nombre: ")
            lista_nombres.append(nombre_nuevo)
                
            edad_nuevo = int(input("Ingrese su edad: "))
            lista_edad.append(edad_nuevo)
            
            membresia_nuevo = int(input("Ingrese el nro de su membresia (1=anual - 2=mensual): "))
            
            while True:
                if membresia_nuevo == 1:
                    lista_membresias.append("Anual")
                    break
                
                elif  membresia_nuevo == 2:  
                    lista_membresias.append("Mensual")
                    break
                else:
                    print("Error. Ingrese una opcion valida\n")
                    membresia_nuevo = int(input("Ingrese el nro de su membresia (1=anual - 2=mensual): "))
                
            lista_membresias.append(membresia_nuevo)
            
            print("Usuario agregado con exito.")
            print("-"*75,"\n")
                    

    
    #Agregar un msotrar la informacion de todos los miembros
        case 2:
            for i in range(len(lista_id)):
                print("{0} - {1} - {2} - {3}".format(lista_id[i],lista_nombres[i],lista_edad[i],lista_membresias[i]))
            print("-"*75,"\n")
            
    #Actualizar el tipo de membresia de un miembro
        case 3:
            id_miembro = int(input("Ingrese el id del miembro a modificar: "))
            indice_id_modificar = -1

            while not id_miembro in lista_id:
                id_miembro= int(input("Ese id no existe en la lista, ingrese uno nuevo: "))
            for i in range(len(lista_id)):
                if id_miembro == lista_id[i]:
                    indice_id_modificar = i
                    break
                
            print("Usuario encontrado:\n"
                  "{0} - {1} - {2} - {3}".format(lista_id[indice_id_modificar],lista_nombres[indice_id_modificar],lista_edad[indice_id_modificar],lista_membresias[indice_id_modificar]))
                    
            if indice_id_modificar != -1:
                
                membresia_nueva = int(input("Ingrese el tipo de membresia nueva para {0} (1=anual - 2=mensual): ".format(lista_nombres[indice_id_modificar])))
                
                while True:
                    if membresia_nueva == 1:
                        lista_membresias[indice_id_modificar] = "Anual"
                        print("\nUsuario actualizado\n")
                        break
                    elif membresia_nueva == 2:
                        lista_membresias[indice_id_modificar] = "Mensual"
                        print("Usuario actualizado\n")
                        break
                    else:
                        membresia_nueva = int(input("Valor invalido.\n Ingrese el tipo de membresia nueva para {0} (1=anual - 2=mensual): ".format(lista_nombres[indice_id_modificar])))
        
            for i in range(len(lista_id)):
                print("{0} - {1} - {2} - {3}".format(lista_id[i],lista_nombres[i],lista_edad[i],lista_membresias[i]))
                
            print('-'*75)
    #Buscar informacion de un miembro
        case 4:
            id_miembro = int(input("Ingrese el id del miembro: "))
            indice_id_modificar = -1

            for i in range(len(lista_id)):
            
                if id_miembro == lista_id[i]:
                    indice_id_modificar = i
                break

            print("{0} - {1} - {2} - {3}".format(lista_id[indice_id_modificar],lista_nombres[indice_id_modificar],lista_edad[indice_id_modificar],lista_membresias[indice_id_modificar]))    
            print("-"*75,"\n")
            
    #Calcular el promedio de edad e los miembros
        case 5:
            
            promedio_edad = sum(lista_edad) / len(lista_edad)
            print("El promedio de edad es: {}\n".format(promedio_edad))
            
            print("-"*75,"\n")
            
            
            
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

                if lista_edad[i] < edad_minima:
                    edad_minima = lista_edad[i]
                    
            for i in lista_edad:
                if i == edad_maxima:
                    lista_edad_maximas.append(i) 

            for i in lista_edad:
                if i == edad_minima:
                    lista_edad_minimas.append(i)
                        
            #Muestro edad maximas
            if len(lista_edad_maximas) == 1:
                for i in range(len(lista_id)):
                    if edad_maxima == lista_edad[i]:
                        print("El miembro mayor es: \n {0} con {1} ".format(lista_nombres[i],lista_edad[i]))
            else:
                print("Los miembros con mayor edad son: \n")
                for i in range(len(lista_id)):
                    if edad_maxima == lista_edad[i]:
                        print("{0} con {1} años ".format(lista_nombres[i],lista_edad[i]))
                        
            #Muestro edad minimas
            if len(lista_edad_minimas) == 1:
                for i in range(len(lista_id)):
                    if edad_minima == lista_edad[i]:
                        print("Miembro mas joven: {0} con {1} ".format(lista_nombres[i],lista_edad[i]))
            else:
                print("Los miembros con menor edad son: ")
                for i in range(len(lista_id)):
                    if edad_minima == lista_edad[i]:
                        print("{0} con {1} años \n".format(lista_nombres[i],lista_edad[i]))
                        
                    
            print("-"*75,"\n")
        case 0:
            print("Salir")
            break
        case other:
            print("Opcion no valida\n")
        
        

