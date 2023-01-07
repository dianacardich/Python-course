from random import randint

palabras_mente = [   #declaramos una variable lista
    'intelecto', 'comprensión','razón', 'juicio',
    'perspicacia', 'astucia', 'talento', 'mente',
    'capacidad', 'materia','cerebro', 'entendimiento', 
    'raciocinio', 'percepción', 'conocimiento', 'consciente',
    'subconsciente', 'ingenio', 'genio'
]

def menterizar(palabra):
    random_pos = randint(0,len(palabras_mente) - 1)
    return f'{palabra} {palabras_mente[random_pos]}'
    

parrafos = int(input("Cantos parrafos de mentes ipsum: ")) #convertimos a un entero

with open('ipsum.txt') as ipsum_original: #con "open" abrimos el fichero ipsum.txt y le ponemos un alias
    objetos = ipsum_original.read().split() #convertimos esas palabras y la guardamos en lista "objetos", .read para que lea el ipsum_original y .split para separar esas palabras 


    for n in range(parrafos):
        mentes_text = list(map(menterizar , objetos))


#las palabras deben llevar un formato
        with open('mente_ipsum.txt','a')as ipsum_mente:
            ipsum_mente.write(' '.join(mentes_text) + '\n\n') 