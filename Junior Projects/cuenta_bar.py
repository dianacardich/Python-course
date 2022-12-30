# programa que se encargue de llevar la cuenta en un bar
class Cuenta:

    menu = {                   #usaremos diccionario, clave - valor.
        
        'vino':4,
        'cerveza':3,
        'nestea':2,
        'pollo':10,
        'carne':15,
        'ensalada':12,
        'postre':6

    }

    def __init__(self):  #init se encarga de crear propiedades por nosotros,
        self.total = 0 #total de la factura
        self.objetos = []  #objetos del menu


    def add(self,objeto):  # añade objeto a esta lista de objetos de arriba
        self.objetos.append(objeto) # metodo append añade esos "objeto" a la lista de objetos
        self.total += self.menu[objeto] # aqui se suma el valor(precio) de cada objeto(producto) de la cuenta

    def print_factura(self,impuesto,servicio): #funcion que imprime el recibo/factura
        impuesto = (impuesto/100)*self.total  #calcular el porcentaje del impuesto
        servicio = (servicio/100)*self.total
        total = self.total + impuesto + servicio #calcular total de totales

        for objeto in self.objetos:  #para c/u objeto de esa lista de objetos
            print(f'{objeto} €{self.menu[objeto]}') #imprime los objetos con su precio
        
        print(f'{"Total"} €{total:.2f}') #imprimir el total de la factura

