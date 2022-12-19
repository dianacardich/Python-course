#Vamos a pedir al usuario que ingrese el significado completo de una organización o concepto y con ello como resultado obtendremos el acrónimo.
acronimo = input("Ingresa una frase: ")
nueva_cadena ="".join([palabra[0] for palabra in acronimo.split()])#split desarma la cadena y la convierte en una lista de palabras,usando el espacio como separador de palabras
print(nueva_cadena)


# Another possible solution 
"""
nueva_cadena = "" 
for p in palabras:
    nueva_cadena = nueva_cadena + p[0] #aqui cada caracter se concatena y se meten en esta nueva variable

print(nueva_cadena) 
"""
