# estructura de control repetitiva: 
# WHILE: repite un bloque de instrucciones mientras una condicion logica sea verdadera

secreto = "dia" # variable secreto donde tenemos una cadena texto
clave = input("dime la clave:") # datos de entrada
while clave != secreto: # mientras esta condicion NO sea verdad
    print("Clave incorrecta!!!")
    otra = input("¿quieres introducir otra clave (S/N)?:")
    if otra.upper()== "N":
        break; # salimos de bucle ya no nos pide la contraseña
    clave = input("dime la clave:")
if clave == secreto:
    print("Bienvenido")
print("programa terminado")

