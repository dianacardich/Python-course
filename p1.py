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
