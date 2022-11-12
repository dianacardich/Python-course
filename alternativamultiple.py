#compruebas varias condiciones
nota = int(input("Dime tu nota:"))
if nota >=1 and nota <=4:
    print("suspenso")
elif nota ==5:
    print("suficiente")
elif nota ==6 or nota == 7:
    print("Bien")
elif nota == 8:
    print ("Notable")
elif nota == 9 or nota == 10:
    print ("Sobresaliente")
else:
    print("nota incorrecta")
print("programa terminado")