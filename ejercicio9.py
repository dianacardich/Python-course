# Realizar un programa que compruebe si una cadena contiene una subcadena.
#las dos cadenas se introducen por teclado.

cad = input("Introduce una cadena:")
subcad = input("Intriduce una subcadena:")

if cad.find(subcad) > -1:
    print("La cadena contiene una subcadena.")
else:
    print("La cadena NO contien la subcadena.")