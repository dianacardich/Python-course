#concatenacion 
#repeticion
#indexación
#longitud
#recorrido

#Las cadenas de caracteres son inmutables(que NO pueden cambiar), puedo usar un metodo para que me devuelva SIN CAMBIAR la cadena.

#Metodos de la cadena de caracteres:
# cuando yo creo una variable cadena, estoy utilizando programacion orientada a objetos, es decir
# una VARIABLE TIPO cadena es un ObJETO de la clase CADENA, este ademas de guardar info puede realizar operaciones
# ----------

#realizar un programa que comprueba si una cadena leida por teclado
#comienza por una subcadena introducida por teclado

cad = input("introduce una cadena:")
subcad = input("introduce una subcadena:")
if cad.startswith(subcad):                          #metodo startwith,está haciendo de condición
    print("La cadena comienza por la subcadena")
else:
    print("La cadena NO comienza por la subcadena")
