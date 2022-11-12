#FOR si se cuando termina mi bucle
# si se cuantas vueltas voy a dar y DONDE-CUANDO termina mi bucle puedo usar FOR , sino uso WHILE
# range (genera una lista de numeros desde el primer valor, hasta el ultimo que le asignemos
'''
for var in range(1,11): #imprime del 1 al 10  #pinta del 1 al 10
    print(var," ",end="")
    
------------

for var in range(10,0,-1): # pinta del 10 al 1 
    print(var," ",end="")
------------

for var in range(2,11,2): # desde el 2 al 10 y que vaya de 2 en 2. Siempre se le quita un numero
    print(var," ",end="")

--------------
'''

#crea un app que pida un # y calcule su factorial (factorial es el producto de todos los enteros entre 1 y el propio #)
#representa por el numero seguido de un signo de exclamacion
# por ejemplo 5! = 1x2x3x4x5=120), WHILE pero se puede con FOR


resultado = 1;
num = int(input("dime un numero:"))
for contador in range(2, num+1):
    resultado = resultado * contador
print("El resultado es", resultado)
