#realizar un algoritmo que muestre la tabla de multiplicar de un numero
#Introducido por teclado

#¿que estructura repetitiva seria mas adecuada?
#Resp: FOR porque sabemos que lo haremos hasta el 10

tabla = int(input("De que numero quieres mostrar la tabla de multiplicar:")) #pedimos el # por teclado
for num in range(1,11):                                                     # le decimos que sera del 1 al 10
    print("%d * %d = %d" %(num,tabla,num*tabla))   #este es el formato que nos dara, ejecutalo Dian                        

