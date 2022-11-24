"""
# 9 Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre
# por pantalla el capital obtenido en la inversión.

invertir = float(input("Ingrese la cantidad a invertir: "))
interesAnual = float(input("Ingrese el interes anual: (%)"))
numAños = int(input("Ingrese el número de años: "))
print("Capital final :  " + str(round(invertir * (interesAnual / 100 + 1) ** numAños, 2)))

#ejercicio 10juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo 
# y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos 
# y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa
#  que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será
#  enviado.

payasos = int(input("ingrese numero de payasos comprados :"))
muñecas = int(input("ingrese cantidad de muñecas compradas: "))

pesoPayaso = payasos * 112
pesoMuñeca = muñecas * 75
pesoTotal = pesoPayaso + pesoMuñeca

print("Se han vendido " ,payasos," payasos y" ,muñecas, " muñecas, el peso total es:" ,pesoTotal) #tambien se puede concatenar pero todos han de ser strings

#11 Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
#Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance
#final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
#depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar 
#por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales

deposito = float(input("Introduce la cantidad de dinero depositado en tu cuenta de ahorros: "))
interes = 0.04 # 4 / 100
primerAño = deposito * (1 + interes)
print("Balance del primer año: " + str(round(primerAño, 2))) #tiene que ir subiendo el balance cogiendo el balance del año anterior 
segundoAño = primerAño *(1 + interes)
print("Balanace del segundo año:" + str(round(segundoAño, 2)))
tercerAño = segundoAño * (1 + interes)
print("Balalnce del tercer año es:" + str(round(tercerAño, 2)))

#12 Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento del 60%. Escribir un programa que comience
#leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuent
#que se le hace por no ser fresca y el coste final total.

panVendido = int(input("Introduce la cantidad de pan pasado vendidas: "))
precioPan = float(3.49)
descuento = 0.6
costeTotal = panVendido * precioPan * (1 - descuento)
print("El coste de una barra fresca es:" + str(precioPan) + "€")
print("El descuento que se le hace por no ser fresca es:" + str(descuento * 100) + "%")
print("El coste final es:" + str(round(costeTotal, 2))+ "€")

#Ejercicios de cadenas 01: Escribir un programa que pregunte el nombre del usuario en la consola
#y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = input("Cual es tu nombre?: ")
numEnt = int(input("Introduce un numero entero: "))
print((nombre + "\n") * numEnt)

#2 Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo 
#del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra 
#del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
import string

nombre= input("introduce tu nombre completo: ")
print(nombre.lower())
print(nombre.upper())
print(string.capwords(nombre)) # esto hace lo mismo sin tener que declarar "import string" print(nombre.title())

 #3 Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por
# pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen
#el nombre.

nombre = input("¿Cual es tu nombre: ")
print (len(nombre))
print(nombre.upper())

#4 Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la
#extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato 
#y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

telf= input("introduce numero de telefono con formato +xx-xxxxxxxxx-xx: ")
print('El numero de telefono es ', telf[4:-3]) #quita 4 posiciones de delante empezando desde cero y siempre quitamos 1. 3posiciones menos desde el final.

#5 Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
frase = input("Introduce una frase: ")
print(frase[::-1])
#6 Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, despues muestre por pantalla
# la misma frase pero con la vocal introducida en mayuscula
frase = input("Introduce una frase: ")
vocal = input("introduce una vocal en minuscula: ")
print(frase.replace(vocal, vocal.upper()))

#7 escribir un programa que pregunte el email del usuario en la consola y muestre por pantalla otro correo eletronico con el
#mismo nombre (la parte de la @) pero con dominio ceu.es.
email =input ("Introduce tu email: ")
print (email[:email.find('@')] + '@ceu.es') # imprime la variable email hasta encontrar (find) el @ (ojito menos una posicion regla explicita), y concatena con @ceu.es
#devuelveme "hasta encontrar  @, por eso [:] esta al inicio.
"""
#8 escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por
#pantalla el numero de euros y el numero de centimos del precio introducido.
precio =input("introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')

#9 escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra , el dia, el mes y el año.
#Adaptar el programa anterior para que tambien funcione cuando el dia el mes se introduzcan con un solo caracter.

fecha = input("Introduce la fecha de tu nacimiento en este formato dd/mm/aaaa: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('dia', dia)
print('mes', mes)
print('año', año)









