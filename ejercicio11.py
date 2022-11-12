#escribe un programa que diga si un numero introducido por teclado esprimo o NO
# PRIMO es aquel que solo es divisible entre él mismo y el 1, el resultado es ENTERO (2 ya que se puede dividor entre 2 y el 1: sus resultado sera un # entero)
# un primo solo debe tener 2 divisores, el (4 tiene 3 por eso no es primo)

es_primo = True
numero_es_primo = int(input("introduce un numero para comprobar si es primo:"))
for num in range(2, numero_es_primo):
    if numero_es_primo % num == 0:
        es_primo = False
        break
if es_primo:
    print("es primo")
else:
    print("no es primo")

