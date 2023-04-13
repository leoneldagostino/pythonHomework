# Ingresar un numero positivo y si es un numero primo que lo imprima y si no lo es que imprima que no es numero primo

numero = int(input("Ingrese un numero: "))
es_primo = True
for num in range(2,numero):
    
    if numero % num == 0:
        print("No es primo {} es divisor".format(num))
        es_primo = False
    
if es_primo:
    print("Es numero primo")