#Algoritmo que muestre la tabla de multiplicar de
#los numeros 1,2,3,4 y 5.

#USAREMOS FOR ANIDADOS (varios for)
#usaremos un FOR para que recorra el bucle de los 5 numeros a multiplicar
#usaremos otro FOR más para que me haga la tabla desde el 1 hasta el 10

for tabla in range(1,6):
    for num in range(1,11):
        print("%d * %d = %d" % (num,tabla,num*tabla))



