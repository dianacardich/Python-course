# pedir el nombre y los apellidos de una persona
# y mostrar las iniciales

nombre = input("Dime tu nombre:")
apellido1 = input("Dime tu primer apellido:")
apellido2 = input("Dime tu segundo apellido:")

inicial = nombre[0]
inicial = inicial + apellido1[0]
inicial = inicial + apellido2[0]
#metodo UPPER para convertir a mayusculas 
inicial = inicial.upper() #ademas nos muestra en mayuscula las iniciales
print("Las iniciales son:", inicial)