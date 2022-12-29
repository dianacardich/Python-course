# Cuando tenemos algun tipo de error porque el usuario introdujo mal un numero 
while True: #bucle que se repetirá hasta que usuario haga la entrada correcta del numero.
    try: #bloque try
        x = int(input("Introduce un numero: "))
        break
    except ValueError:
        print ("Debes introducir un numero")