#dados dos variables numericas A y B, que el usuario debe teclear
#se pide realizar un algoritmo que intercambie los valores de ambas
# y muestre cuanto valen al final las dos variables

a = int(input("Introduce el valor de la variable A:"))
b = int(input("Introduce el valor de la variable B:"))
aux = a
a = b
b = aux # hemos intercambiado el valor de las variables
print("Nuevo valor de a:", a)
print("Nuevo valor de b:", b)



