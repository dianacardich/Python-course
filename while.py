# estructura de control REPETITIVA: cuando NO SE cuando termina mi bucle
# WHILE: repite un bloque de instrucciones mientras una condicion logica sea verdadera, 
'''
secreto = "dia"                         # variable secreto donde tenemos una cadena texto
clave = input("dime la clave:")         # datos de entrada
while clave != secreto:                 # mientras esta condicion NO sea verdad
    print("Clave incorrecta!!!")
    clave = input ("Dime la clave:")    # VUELVE a pedirme la clave hasta que sea correcta, para decirte Bienvenido
print("Bienvenido")
print("programa terminado")

'''
#crea un app que pida un # y calcule su factorial (factorial es el producto de todos los enteros entre 1 y el propio #)
#representa por el numero seguido de un signo de exclamacion
# por ejemplo 5! = 1x2x3x4x5=120), WHILE pero se puede con FOR

resultado = 1;
num = int(input("dime un numero:"))
contador = 2;
while contador <= num:
    resultado = resultado * contador
    contador = contador + 1
print("El resultado es", resultado)


