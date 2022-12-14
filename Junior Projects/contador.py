#Preguntamos al usuario en que está pensando. Cuando se introduce la respuesta, realizará el conteo de palabras en la sentencia
#e imprimimos en la salida el resultado.

user = input("What are you thinking? ")
 # separamos con split para que cuente por palabra
result = len(user.split())
print("Very well you have shown me your thoughts in  " + str(result) + " words.")
