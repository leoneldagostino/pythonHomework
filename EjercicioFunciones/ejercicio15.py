'''

15.
Crear una función que recibe una lista de diccionarios con información de películas (título, género, director) 
y devuelve un diccionario con la cantidad de películas por género.

'''

lista_peliculas =\
[
  {
    "titulo":"Star Wars: Episodio 1",
    "genero":"Ciencia ficcion",
    "director":"George Lucas"    
  },
  {
    "titulo":"El robo del siglo",
    "genero":"Suspenso",
    "director":"Ariel Winograd"
  },
  {
      "titulo":"El lobo de Wall Street",
      "genero":"Drama",
      "director":"Martin Scorsese"
  },
  {
      "titulo":"El lobo de Wall Street",
      "genero":"Drama",
      "director":"Martin Scorsese"
  },
  {
      "titulo":"El lobo de Wall Street",
      "genero":"Drama",
      "director":"Martin Scorsese"
  }
]

def info_pelis(lista_peliculas):
    diccionario_generos = {}
    
    for genero in lista_peliculas:
        cont_genero = 0
        valor_genero = genero.get("genero")
        for cuenta_genero in lista_peliculas:
            
            comparar_genero = cuenta_genero.get("genero")
            if comparar_genero == valor_genero:
                cont_genero +=1
                diccionario_generos.update({valor_genero : cont_genero})
    
    return diccionario_generos
            
        
        

print(info_pelis(lista_peliculas))