# Escribe un programa que lea una cadena y devueva un diccionario con la cantidad
# de apariciones de cada caracter en la cadena

dict = {}   #diccionario vacio
cadena = (input("Introduce una cadena de texto: ")) # pedimos la cadena po teclado
for caracter in cadena: # recorrer la cadena para ver c/u de los caracteres
    if caracter in dict: # si ya tenemos un elemento en el diccionario cuya clave sea el caracter, 
        dict[caracter]+=1 # incrementamos el contador (ese valor)
    else:               # y si no esta en el diccionario porque es nuevo el "caracter"
        dict[caracter]=1  #inicializamos a 1 porque es una nueva aparicion

for clave,valor in dict.items(): # esto se repite por c/u de los caractreres que aparecen, y recorremos el diccionario
    print (clave, "->", valor) #pintamos la clave y el valor 

