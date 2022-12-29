# Una excepcion puede provocar varias excepciones 

cad = input("Dime un numero: ")
try:
    print ( 10/int(cad))
except ValueError:
    print("No se puede convertir a entero.")
except ZeroDivisionError:  # por si el usuario pone un 0 
    print("No se puede dividir por cero")
else: 
    print("Se ha producido otro error")
finally:
    print("Se ejecuta siempre al final de la excepcion") # el "finally se ejecuta al final"