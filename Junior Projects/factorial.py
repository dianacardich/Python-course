# Funciones Iterativas 
def factorial(n):  #funcion para calcular factorial de un numero 
    """Calcula el factorial de un numero"""
    resultado = 1
    for i in range(1, n+1):
        resultado*=i
    return resultado

# debemos importar factorial para poder ejecutar este ejercicio

# from **** import factorial (en los asteriscos se pone el nombre del fichero), esto en la terminal
