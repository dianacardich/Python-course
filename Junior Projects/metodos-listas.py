#realice un programa que incialice a una lista con 10 valores aleatorios
#posteriormente muestre en pantalla cada elemento de la lista junto a su cuadrado y su cubo.

import random       #libreria random que nos genera numeros aleatorios
lista_numeros = []
# Primer recorrido para leer la lista, bucle for porque sabemos cuando termina
for indice in range(1,11):
    lista_numeros.append(random.randint(1,10))  #randint genera num aletarios 
## Segundo recorrido para mostrar resultado
for numero in lista_numeros:
    print(numero," ",numero ** 2," ", numero ** 3)