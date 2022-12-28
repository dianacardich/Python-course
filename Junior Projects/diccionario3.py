# Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas.
#  El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a
#  partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa
# nos preguntará si queremos hacer otra consulta.

diccionario = {'banana':2, 'apple':4.5 , 'orange':3}
while True:
    fruta= input("Dime la fruta que has vendido: ")
    if fruta.lower() not in diccionario:
        print("Fruta no existe.")
    else:
        cantidad = int(input("Dime la cantidad de frutas que has vendido:"))
        print("El precio es de %f" % (cantidad * diccionario[fruta.lower()]))
    opcion = input("¿Quieres vender otra fruta (s/n)")
    while opcion.lower() != "s" and opcion.lower() != "n":
        opcion = input("¿Quieres vender otra fruta (s/n)")
    if opcion.lower() == "n":
        break





