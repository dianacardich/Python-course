# Funcion EsMultiplo: Recibe dos numeros e indica si el primero es multiplo del segundo.
# para ello calculo el resto de la division, s es 0 es multiplo.
# Parámetros de entrada:dos numeros
# Dato envuelto: multiplo: Valor lógico verdadero si el primero es multiplo del segundo, Falso en caso contrario.


def esmultiplo(num1, num2):  # esta funcion entera la puedo volver a reutilizar cuando tenga otro problema que resolver
    if num1 % num2 == 0:
        return True
    else:
        return False


#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro.
# Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
if esmultiplo (numero1, numero2):
    print(numero1, "Es multiplo de", numero2)
else:
    print(numero1, "no es multiplo de", numero2)
