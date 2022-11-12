#escribe un programa que pida una fecha(dia,mes y año) y diga si la fecha es correcta o no.

dia = int(input("Introduce el dia:"))
mes = int(input("Introduce el mes:"))
year = int(input("Introduce el year:"))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12: #meses que tienen 31 dias 
    dias_del_mes = 31;
elif mes == 4 or mes == 6 or mes == 9 or mes == 11: #meses que tienen 30 dias
    dias_del_mes = 30;
elif mes == 2: 
    if (year % 4 == 0 and not (year % 100 == 0)) or year % 400 ==0: 
        dias_del_mes = 29; # mes que es bisiesto
    else:
        dias_del_mes = 28;
else:
        print("Fecha incorrecta")

if dia < 0 or dia > dias_del_mes:
    print("Fecha incorrecta")
else:
    print("Fecha correcta")   
