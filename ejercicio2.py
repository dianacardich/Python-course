# Algoritmo que pida un numero y diga si es positivo, negativo o 0.
# alternativa multiple

numero = int(input("Dime el numero:"))
if numero == 0:
    print("Es igual a 0")
else:
    if numero > 0:
        print("es positivo")
    else:
        print("es negativo")


# se puede hacer igual de la misma manera alternativa multiple
""" numero = int(input("Dime el numero:"))
if numero == 0:
    print("Es igual a 0")
elif numero > 0:
    print("es positivo")
else:
    print("es negativo") """