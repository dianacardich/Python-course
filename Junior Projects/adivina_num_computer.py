#computadora debe averiguar el numero que le diga el usuario

import random

def adivina_el_num_computer(x):
    
    print("==================")
    print("Bienvenido(a) al juego")
    print("======================")
    print(f"Selecciona un numero entre 1 y {x} para que la computadora intente adivinarlo..")


    limite_inferior = 1 
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        #generar una prediccion
        if limite_inferior != limite_superior: # [1, 10]
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior # tambien podría ser el limite superior.

        # Obtener respuesta del usuario
        

