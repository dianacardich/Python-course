# escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducdio "pepe" y "asdsd" se indica " has entrado al sistema"
# sino se da error

usuario = input("introduce el usuario:")
password = input ("Introduce el password:")
if usuario == "diana" and password == "cardich":
    print("has entrado al sistema")
else:
    print("usuario/password incorrecto")
    

