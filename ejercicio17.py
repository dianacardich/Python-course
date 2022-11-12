#un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos
#el tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
# Escribir un algoritmo que determine la hora de llegada a la ciudad 

horapartida = int(input("Dime la hora de partida:"))
minpartida = int(input("Dime los minutos de partida:"))
segpartida = int(input("Dime los segundos de partida:"))
segviaje = int(input("Tiempo que has tardado en segundos:"))
# convierto la hora de salida en segundos
seginicial = horapartida * 3600 + minpartida*60 + segpartida;
# le sumo los segundos que he tardado
segfinal = seginicial + segviaje;
#convierto los segundos totales a hora, minuto y segundos.
horallegada = segfinal // 3600; # // division entera
minllegada = (segfinal % 3600) // 60; # % operador modulo me quedo solo con la parte entera 
segllegada = (segfinal % 3600) % 60; # % me quedo con el resto del resto 
# Muestro de hora de llegada 
print("Hora de llegada")
print(horallegada,":",minllegada,":",segllegada)

