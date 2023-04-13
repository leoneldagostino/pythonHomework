#Dado un número entero n,
# imprimir la secuencia de números pares menores o iguales a n.

numero = int(input("Ingrese un numero: "))

for num in range(0,numero):
    if num % 2 == 0:
        print(num)