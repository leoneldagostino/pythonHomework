#dada una lista de palabras, imprimir la cantidad de vocales en  la lista

palabras = ["hola","palabras","lista","de"]
vocales = ['a','e','i','o','u']
cont_vocales = 0

for p in palabras:
    for letra in p:
        if letra in vocales:
            cont_vocales += 1

print("la cantidad de vocales que hay son {}".format(cont_vocales))
