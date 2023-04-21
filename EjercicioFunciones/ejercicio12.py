'''

12.
Crea una función que reciba dos listas de nombres, y devuelva una lista con los nombres que aparecen en ambas listas

'''


def buscar_nombres(lista_1,lista_2):
    lista_nombres = []
    
    for nombre in lista_1:
        nom = nombre
        for nombres in lista_2:
            if nombres == nom:
                lista_nombres.append(nom)
                
    return lista_nombres

lista_nombres_1 = ["pedro","diego","leo","fede","jorge"]
lista_nombres_2 = ["diego","leo","lisandro","messi"]


print(buscar_nombres(lista_nombres_1,lista_nombres_2))