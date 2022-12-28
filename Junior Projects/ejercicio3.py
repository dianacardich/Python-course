#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
#A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

notas = []                                                       #lista vacía donde voy guardando las notas
for indice in range(1,6):                                        # voy a decir que son 5 notas (dentro de ese rango)
    while True:                                                  # validar
        nota = int(input("Introduce la nota %d:" % indice))      # voy a pedir 5 notas, indice para que diga introduce la nota 1,la 2 ,la 3
        if nota>=0 and nota <=10: break                          #validar que sean >=0 and <=10
    notas.append(nota)                                           # con append las añado a la lista


# Mostrar resultados 

print("Notas: ",end="")
for nota in notas:
    print(nota, " ", end="")
print()
print("Nota media: ", sum(notas)/len(notas))
print("Nota max: ",max(notas))
print("Nota min: ",min(notas))


