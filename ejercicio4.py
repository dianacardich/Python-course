# suponiendo que hemos introducido una cadena por teclado que representa una frase (palabtas separadas por espacios),
#realiza un programa que cuente cuantas palabras tiene

cont = 0
posicion = 0
cad = input("Introduce una frase:")
#elimino los posibles espacios que haya al principio y al final de la cadena
cad = cad.strip()
#voy buscando los espacios
posicion = cad.find(" ", posicion)
while posicion != -1:
    cont = cont + 1
    #no tengo en cuenta los posibles espacios entre las palabras
    while cad[posicion + 1] == " ":
        posicion = posicion + 1
    posicion = cad.find(" ",posicion + 1)
print("La frase tiene", cont + 1, "palabras.")




