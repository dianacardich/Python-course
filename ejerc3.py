#pide una cadena y un caracter por teclado
#valida que sea un caracter y muestra cuantas veces aparece el caracter en la cadena.

cad = input("introduce una cadena:")
while True:
    car = input("introduce un caracter:")
    if len(car)>1: #validamos que sea solo 1
        print("Me tienes que dar un solo caracter")
    if len(car) == 1: break
print ("en la cadena",cad,"aparecen",cad.count(car), "veces el caracter",car)

