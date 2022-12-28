#Diseñar el algoritmo correspondiente a un programa, que:

# - Crea una tabla (lista con dos dimensiones) 5x5 enteros.
# - Carga la tabla con valores numericos enteros
# - Suma todos los elementos de cada fla y todos los elementos de cada columna

tabla = [] # tengo 1 lista
for indice_fila in range(1,6):
    fila = [] # variable tipo lista 
    for indice_col in range(1,6): # bucle para recorrer los elementos de c/u columnas (lista)
        fila.append(int(input("Introduce el número de la fila %d y columna %d:" % (indice_fila,indice_col)))) # voy añadiendo elementos que pido por teclado con append
    tabla.append(fila) #añado esa lista anterior a la tabla con otro append

#Suma las filas (las listas)
indice_fila = 1  #variable que me ira diciendo la suma de c/u de las filas
for fila in tabla: #recorro la fila
    print("La suma de los elementos de la fila %d es %d" % (indice_fila,sum(fila))) #mostrar la suma de la fila 
    indice_fila +=1 # aqui lo incremento

# Suma las columnas
for indice_col in range(1,6): #no recorro una lista
    suma = 0 # acumulador que me ponga a 0
    for fila in tabla: #recorro c/u de las filas
        suma = suma + fila[indice_col - 1] #me quedo con los elementos que me interesan
    print("La suma de los elementos de la columna %d es %d" % (indice_col,suma)) #mostrar la suma de las columnas
