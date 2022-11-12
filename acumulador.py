# ACUMULADOR es una variable numerica que permite ir acumulando operaciones, permite hace operaciones PARCIALES
suma = 0
for var in range(1,6) :
    num = int(input("Dime un numero:"))
    if num % 2 == 0:                                # si la variable num entre dos es igual a cero es PAR entonces 
        suma = suma + num                           #se acumula. cada ves que encuentre un # par lo SUMA
print("La suma de los numeros pares es ", suma)
