#CONTADOR es una VARIABLE entera, la usamos para CONTAR cuando ocurre un SUCESO, se incrementa o decrementa

cont = 0;                                           # el contador se INICIALIZA
for var in range(1,6):                              # me pide 5 numeros
    num  = int(input("Dime un numero:"))
    if num % 2 == 0: 
        cont = cont + 1                             # el contador se incrementa
print ("Has introducido ",cont," numeros pares.")