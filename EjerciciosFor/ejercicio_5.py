#dada una lista de numeros, imprimir el numero de lista
# < >

numeros = [4,2,1,5,6,8,21,42,12]
numero_mas_bajo = numeros[0]
for n in numeros: 
    if n < numero_mas_bajo:
        numero_mas_bajo = n
        
print(numero_mas_bajo)