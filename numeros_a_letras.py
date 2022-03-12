def respuestas():
    if letra == 0:
        print('a')
    elif letra == 1:
        print('b')
    elif letra == 2:
        print('c')
    elif letra == 3:
        print('d')
    elif letra == 4:
        print('e')
    elif letra == 5:
        print('f')
    elif letra == 6:
        print('g')
    elif letra == 7:
        print('h')
    elif letra == 8:
        print('i')
    elif letra == 9:
        print('j')
    elif letra == 10:
        print('k')
    elif letra == 11:
        print('l')
    elif letra == 12:
        print('m')
    elif letra == 13:
        print('n')
    elif letra == 14:
        print('o')
    elif letra == 15:
        print('p')
    elif letra == 16:
        print('q')
    elif letra == 17:
        print('r')
    elif letra == 18:
        print('s')
    elif letra == 19:
        print('t')
    elif letra == 20:
        print('u')
    elif letra == 21:
        print('v')
    elif letra == 22:
        print('w')
    elif letra == 23:
        print('x')
    elif letra == 24:
        print('y')
    elif letra == 25:
        print('z')

def respuestas2():
    if residuo == 0:
        print('a')
    elif residuo == 1:
        print('b')
    elif residuo == 2:
        print('c')
    elif residuo == 3:
        print('d')
    elif residuo == 4:
        print('e')
    elif residuo == 5:
        print('f')
    elif residuo == 6:
        print('g')
    elif residuo == 7:
        print('h')
    elif residuo == 8:
        print('i')
    elif residuo == 9:
        print('j')
    elif residuo == 10:
        print('k')
    elif residuo == 11:
        print('l')
    elif residuo == 12:
        print('m')
    elif residuo == 13:
        print('n')
    elif residuo == 14:
        print('o')
    elif residuo == 15:
        print('p')
    elif residuo == 16:
        print('q')
    elif residuo == 17:
        print('r')
    elif residuo == 18:
        print('s')
    elif residuo == 19:
        print('t')
    elif residuo == 20:
        print('u')
    elif residuo == 21:
        print('v')
    elif residuo == 22:
        print('w')
    elif residuo == 23:
        print('x')
    elif residuo == 24:
        print('y')
    elif residuo == 25:
        print('z')
    


respuesta = """
hola cambia numeros por letras
elije un numero que quieras cambiar: 

"""

numero = int(input(respuesta))
if numero == 0:
    print('a')
elif numero == 1:
    print('b')
elif numero == 2:
    print('c')
elif numero == 3:
    print('d')
elif numero == 4:
    print('e')
elif numero == 5:
    print('f')
elif numero == 6:
    print('g')
elif numero == 7:
    print('h')
elif numero == 8:
    print('i')
elif numero == 9:
    print('j')
elif numero == 10:
    print('k')
elif numero == 11:
    print('l')
elif numero == 12:
    print('m')
elif numero == 13:
    print('n')
elif numero == 14:
    print('o')
elif numero == 15:
    print('p')
elif numero == 16:
    print('q')
elif numero == 17:
    print('r')
elif numero == 18:
    print('s')
elif numero == 19:
    print('t')
elif numero == 20:
    print('u')
elif numero == 21:
    print('v')
elif numero == 22:
    print('w')
elif numero == 23:
    print('x')
elif numero == 24:
    print('y')
elif numero == 25:
    print('z')
else:
    letra = (numero / 26) - 1
    residuo = numero % 26
    letra = int(letra)
    respuestas()
    respuestas2()


        
        
