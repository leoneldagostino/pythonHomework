# ingrese una letra y tiene que imprimir si es una vocal o consonante 

letra = input("Ingrese una letra: ")

if letra == "a": 
    print("Es una vocal")
elif letra == "e": 
    print("Es una vocal")
elif letra == "i": 
    print("Es una vocal")
elif letra == "o": 
    print("Es una vocal")
elif letra == "u": 
    print("Es una vocal")
else:
    print("Es una consonante")
    
vocales = ['a','e','i','o','u']

letr = input("Ingrese una letra: ")
es_vocal = False
for l in vocales:
    if l == letr:
        print("Es una vocal")
        es_vocal = True
    

if es_vocal == False:

    print("Es una consonante")

    
