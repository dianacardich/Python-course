# Concatenar cadenas de caracteres.
# Supongamos que queremos crear una cadena quediga:
# Aprende a programar con -------.

# organizacion = "freeCodeCamp"

# print("Aprende a programar con " + organizacion )
# print("Aprende a programar con {}".format(organizacion)) # concatenar cadenad o reemplazar valores en la cadena de caracteres
# print(f"Aprende a programar con {organizacion}") # f-string 

# Mad Libs (Historias Locas)
adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo (prural): ")

madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. Aprende a {verbo2} con freeCodeCamp y alcanca tus {sustantivo_plural}"

print(madlib)