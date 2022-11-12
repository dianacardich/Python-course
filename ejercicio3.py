#algoritmo que pida #s hasta que se introduzca un cero. Debe imprimir la suma 
#y la media de todos los numeros introducidos.

#usamos WHILE porque NO se cuando termira el bucle
'''
suma = 0
cont = 0

#con el WHILE si el primer numero es 0 no va entrar en el bucle
num = int(input("Numero (0 para salir):"))      #datos de entrada   
while num !=0:                                  #condición  
    suma = suma + num                           #acumular el #
    cont = cont + 1                             # cuento la cantidad de #s que introducido
    num = int(input("Numero (0 para salir):"))  #volver a pedir dato de entrada


#si el cont = 0 no puedo realizar la division
if cont > 0:
    media = suma / cont
else:
    media = 0

print("Suma:", suma)
print("Media:", media)

'''

# con FOR

suma = 0
cont = 0
while True: #true al menos entramos 1 ves al dato
    num = int (input("Numero (0 para salir):"))
    suma = suma + num
    #Si num = 0 no debemos tenerlo en cuenta para calcular la media 
    if num !=0: # el cero no lo voy a contar
        cont = cont + 1
    if num == 0:
        break #salgo del bucle
    #Si cont=0 no puedo realizar la division
    if cont !=0:
        media = suma / cont
    else:
        media = 0




