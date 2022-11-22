#1 programa que muestre por pantalla la cadena Hola mundo!
print("Hola mundo!")

#2: variable que almacena la cadena Hola Mundo, y que muestre por pantalla el contenido de la variable
sayHello = ("Hola Mundo")
print(sayHello)

#3 Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo 
# introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario 
# haya introducido.

name = str(input("Dime tu nombre:"))
print("Hola"+ " " + name)

#4 Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética
print(((3+2)/ (2 * 5)) ** 2)

#5 Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.

horas = float(input("Horas trabajadas: "))
coste = float(input("Coste por hora:"))
paga = (horas * coste)
print("Tu paga es", paga)

# 6 Escribir un programa que lea un entero positivo,n , introducido por el usuario y después muestre en
#  pantalla la suma de todos los enteros desde 1 hasta n  La suma de los  primeros enteros positivos puede
#  ser calculada de la siguiente forma:

n = int(input("Ingrese un numero entero:"))
suma = n * (n + 1) / 2
print("La suma de los primeros enteros desde 1 hasta " + str(n) + " es " + str(suma))

# 7 Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal
#  y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice
#  de masa corporal calculado redondeado con dos decimales.



peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))
imc = round((peso/estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))
