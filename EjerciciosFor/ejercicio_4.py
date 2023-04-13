#dado un numero,
#imprimir la suma de numeros impares menores al numero

num = int(input("Ingrese un numero: "))
suma_impares = 0

for numero in range(0,num):
    if numero % 2 != 0:
        suma_impares += 1
        
print("Los numeros impares totales son: {}".format(suma_impares))