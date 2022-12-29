#funciones recursivas, su caracteristica es que dentro de la funcion hay una llamada a la misma funcion, linea 7
#  el factorial de un numero es el numero multiplicado por el factorial del numero menos 1 
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))