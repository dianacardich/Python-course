# usuario debe adivinar el numero que le diga la computadora

import random   #aleatorio 


def adivina_el_numero (x): #definimos una función

    print("=======================")
    print(" Bienvenido(a) al juego")
    print("=======================")
    print("Tu meya es adivinar el numero generado por la computadora. ")

    numero_aleatorio = random.randint(1,x)  #ran int genera un integrer aleatorio entre 1 y x

    prediccion = 0
    
    while  prediccion != numero_aleatorio: #mientras la prediccion sea distinto (no sea igual) al num_aleatorio
        # usuario ingresa un numero
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: ")) #f-string reemplaza un valor de una variable en esta cadena
        
        if prediccion < numero_aleatorio:
            print("Intenta otra. Este numero es muy pequeño")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. Este numero es muy grande.")


    print(f"¡Felicitaciones! Adivinaste el numero {numero_aleatorio} correctamente.")


adivina_el_numero(10)
