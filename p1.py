# 9 Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre
# por pantalla el capital obtenido en la inversión.

invertir = float(input("Ingrese la cantidad a invertir: "))
interesAnual = float(input("Ingrese el interes anual: (%)"))
numAños = int(input("Ingrese el número de años: "))
print("Capital final :  " + str(round(invertir * (interesAnual / 100 + 1) ** numAños, 2)))

