# INDICADOR es VARIABLE logica, recuerda o indica SUCESOS - tipo BOOLEAN

indicador = False;                              #aqui se inicializa a un valor logico, FALSO= no he sucedido no hemos introducido, ningun par
for var in range(1,6) :
    num = int(input("dime un numero:"))
    if num % 2 == 0:                            #en el momento que 1 de ellos sea PAR,
        indicador = True                        # suceso cambiamos su valor
if indicador:                                   #comprobamos si el suceso ha ocurrido
    print("Has introducido algun numero par") 
else: 
    print("No has introducido algun numero par")