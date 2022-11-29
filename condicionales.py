"""
# 1 escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no
edad = int(input("¿Cuantos años tienes: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("eres menor de edad")

# 2 escribir un programa que almacene la cadena de carateres "contraseña" en una variable, pregunte al usuario por la contraseña
# e imptima por pantalla si la contraseña introducida coundide con la guardada en la variable sin tener en cuenta mayusculas o minusculas.

passw = "contraseña"
usuario = input("cual es tu password?: ")
if passw == usuario.lower():
    print("la constraseña coincide")
else: 
    print("la contraseña no coincide")

#3escribir un programa que pida al usuario dos numeros y muestre por pantalla si division. 
#Si el divisor es cero el prgrama debe mostar un error.
dividendo= int(input("Introduce dividendo: "))
divisor= int(input("introduce divisor: "))
if divisor == 0:
    print("Error no se puede dividir por 0.")
else:
    print(dividendo/divisor) #definimos la division aqui porque es cuando ya ha cumplido los requisitos

#4 escribir un programa que pida al usuario un numero entero y muestre por pantalla si es par o impar
numero = int(input("Introduce un numero entero: "))
if (numero % 2) == 0:
    print("The provided number is even(par) ")
else:
    print("The provided number is odd(impar).")
  
#5 para tributar un determinado impuesto debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000€ mensuales.
#Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene
# que tributar o no.

edad = int(input("cuantos años tienes?: "))
ingresos = float(input("Ingrese sus ingresos mensuales: "))
if edad > 16 and ingresos >= 1000:
    print("El usuario puede tributar.")
else:
    print("El usuario no tiene que tributar.")

#6 Los alumnos de un curso se han dividido en dos grupos , A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres
# con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa
#que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
    
name = input("Como te llamas?: ")
sexo = input("Cual es tu sexo?: ")
if sexo == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else: 
    if name.lower() > "n":
        group = "A"
    else: 
        group = "B"
print("Tu grupo es " + group)

#7 escribir un programa que pregunte al usuario su renta anual y muestrepor pantalla el tipo impositivo que le corresponde.

renta = float(input("Cual es tu renta anual?: "))
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45

print("Tienes que pagar: " , renta * tipo / 100, "€")
 
#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
#traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4. o 0.6, pero no valores intermedios entre las cifras
# mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€
# multiplicada por la puntuación del nivel.

inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
beneficio = 2400

puntos = float(input("Introduce tu puntuacion: "))
#clasificacion por niveles de rendimiento 
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "aceptable"
elif puntos >= 0.6:
    nivel = "meritorio"
else: 
    nivel = ""
# Mostrar nivel de rendimiento 
if nivel == "":
    print("Esta puntuacion no es válida.")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * beneficio)) #%.2f esta especificando que el numero que viene a continuacion es con coma flotante con hasta 2 decimales

#9 escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automatica el precio que debe cobrar a sus clientes
#por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis
# si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.


edad = int(input("Cuantos años tienes?: "))
#decicison del precio en funcion a la edad
if edad < 4:
    entrada = 0
elif edad <= 18:
    entrada = 5
else: 
    entrada = 10
#mostrar precio
print("Debes de pagar por la entrada " + str(entrada), "€.")
"""
"""
EJERCICIO 9
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
    * Ingredientes vegetarianos: Pimiento y tofu.
    * Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes
 disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar
 por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

"""
#Presentacion del menu con los tipos de pizza
print("Bienvenido a la pizzeria Diana Napoli. \nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipoPizza = input("Introduce el numero correspondiente al tipo de pizza que quieres:")
#decisión sobre el tipo de pizza
if tipoPizza == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\ 2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else:
        print("tofu")
else:
    print("Ingredientes de pizzas NO vegetarianas\n\t1- Peperoni\n\t2- Jamon\n\t3- Salmon\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza NO vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "2":
        print("jamon")
    else:
        print("salmon")








