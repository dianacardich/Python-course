#imprime los pares dentro del 0 y menores que 10
cont = 0
while cont<10:
    cont = cont + 1
    if cont % 2 == 1: # contador es impar
        continue
    print(cont)