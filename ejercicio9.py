# algoritmo que pida tres numeros y los muestre ordenador de mayor a menor.

num1 = int(input("Introduce el primer numero:"))
num2 = int(input("Introduce el segundo numero:"))
num3 = int(input("Introduce el tercer numero:"))

if num1>num2 and num1>num3:
    if num2>num3:
        print(num1,num2,num3)
    else:
        print(num1,num2,num3)
if num2>num1 and num2>num3:
    if num1>num3:
        print(num2,num1,num3)
    else:
        print(num2,num3,num1)
if num3>num1 and num3>num2:
    if num1>num2:
        print(num3,num1,num2)
    else:
        print(num3,num2,num1)

#averiguar si esto se puede hacer con alternativa muliple "elif"



