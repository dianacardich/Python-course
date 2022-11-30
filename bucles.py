#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""
word = input("introduce una palabra: ")
for i in range(10):
    print(word)

#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
age = int(input("Cuantos años tienes?: "))
for i in range(age):
    print("Has cumplido " + str(i+1) + " años")

#3 Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

number = int(input("Introduce un numero entero positivo: "))
for i in range(1, number+1, 2): # que empieze desde el 1 , que al numero le vaya sumando 1, y que al dividirlo entre 2 el resto de cero.
    print (i, end=", ")
"""
#4 Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

number = int(input("Introduce un numero entero: "))
for i in range(0, number+1):
        print(str(number-i), end=", ")