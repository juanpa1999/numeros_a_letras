respuesta = """
hola cambia numeros por letras
elije un numero que quieras cambiar: 

""" 
numero = int(input(respuesta))
cosciente = numero
def imprimir():
    resultado2 = numero
    cosciente = int(resultado2 % 26)
    if cosciente == 0:
        print('a')
    elif cosciente == 1:
        print('b')
    elif cosciente == 2:
        print('c')
    elif cosciente == 3:
        print('d')
    elif cosciente == 4:
        print('e')
    elif cosciente == 5:
        print('f')
    elif cosciente == 6:
        print('g')
    elif cosciente == 7:
        print('h')
    elif cosciente == 8:
        print('i')
    elif cosciente == 9:
        print('j')
    elif cosciente == 10:
        print('k')
    elif cosciente == 11:
        print('l')
    elif cosciente == 12:
       print('m')
    elif cosciente == 13:
        print('n')
    elif cosciente == 14:
        print('o')
    elif cosciente == 15:
        print('p')
    elif cosciente == 16:
        print('q')
    elif cosciente == 17:
        print('r')
    elif cosciente == 18:
        print('s')
    elif cosciente == 19:
        print('t')
    elif cosciente == 20:
        print('u')
    elif cosciente == 21:
        print('v')
    elif cosciente == 22:
        print('w')
    elif cosciente == 23:
        print('x')
    elif cosciente == 24:
        print('y')
    elif cosciente == 25:
        print('z')
    while resultado2 > 27:
        resultado2 = int(resultado2 / 26 - 1)
        cosciente = int(resultado2 % 26)
        if cosciente == 0:
            print('a')
        elif cosciente == 1:
            print('b')
        elif cosciente == 2:
            print('c')
        elif cosciente == 3:
            print('d')
        elif cosciente == 4:
            print('e')
        elif cosciente == 5:
            print('f')
        elif cosciente == 6:
            print('g')
        elif cosciente == 7:
            print('h')
        elif cosciente == 8:
            print('i')
        elif cosciente == 9:
            print('j')
        elif cosciente == 10:
            print('k')
        elif cosciente == 11:
            print('l')
        elif cosciente == 12:
           print('m')
        elif cosciente == 13:
            print('n')
        elif cosciente == 14:
            print('o')
        elif cosciente == 15:
            print('p')
        elif cosciente == 16:
            print('q')
        elif cosciente == 17:
            print('r')
        elif cosciente == 18:
            print('s')
        elif cosciente == 19:
            print('t')
        elif cosciente == 20:
            print('u')
        elif cosciente == 21:
            print('v')
        elif cosciente == 22:
            print('w')
        elif cosciente == 23:
            print('x')
        elif cosciente == 24:
            print('y')
        elif cosciente == 25:
            print('z')
        


if __name__ == '__main__':
    imprimir()