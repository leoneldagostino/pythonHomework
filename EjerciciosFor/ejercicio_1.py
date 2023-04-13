#Dada una lista de números, imprimir el número más grande de la lista.


lista_numeros = list(range(1,50,3))
numero_mas_grande = lista_numeros[0]

for numero in lista_numeros:
    if numero > numero_mas_grande:
        numero_mas_grande = numero
print(numero_mas_grande)
    
    

    