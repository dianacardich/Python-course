"""
# 1 escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no
edad = int(input("¿Cuantos años tienes: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("eres menor de edad")

# 2 escribir un programa que almacene la cadena de carateres "contraseña" en una variable, pregunte al usuario por la contraseña
# e imptima por pantalla si la contraseña introducida coundide con la guardada en la variable sin tener en cuenta mayusculas o minusculas.

passw = "contraseña"
usuario = input("cual es tu password?: ")
if passw == usuario.lower():
    print("la constraseña coincide")
else: 
    print("la contraseña no coincide")

#3escribir un programa que pida al usuario dos numeros y muestre por pantalla si division. 
#Si el divisor es cero el prgrama debe mostar un error.
dividendo= int(input("Introduce dividendo: "))
divisor= int(input("introduce divisor: "))
if divisor == 0:
    print("Error no se puede dividir por 0.")
else:
    print(dividendo/divisor) #definimos la division aqui porque es cuando ya ha cumplido los requisitos

#4 escribir un programa que pida al usuario un numero entero y muestre por pantalla si es par o impar
numero = int(input("Introduce un numero entero: "))
if (numero % 2) == 0:
    print("The provided number is even(par) ")
else:
    print("The provided number is odd(impar).")
"""   
#5 para tributar un determinado impuesto debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000€ mensuales.
#Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene
# que tributar o no.

edad = int(input("cuantos años tienes?: "))
ingresos = float(input("Ingrese sus ingresos mensuales: "))
if edad > 16 and ingresos >= 1000:
    print("El usuario puede tributar.")
else:
    print("El usuario no tiene que tributar.")




