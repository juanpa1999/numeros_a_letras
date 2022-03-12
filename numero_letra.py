def respuestas3():
    if resultado == 0:
        print('a')
    elif resultado == 1:
        print('b')
    elif resultado == 2:
        print('c')
    elif resultado == 3:
        print('d')
    elif resultado == 4:
        print('e')
    elif resultado == 5:
        print('f')
    elif resultado == 6:
        print('g')
    elif resultado == 7:
        print('h')
    elif resultado == 8:
        print('i')
    elif resultado == 9:
        print('j')
    elif resultado == 10:
        print('k')
    elif resultado == 11:
        print('l')
    elif resultado == 12:
       print('m')
    elif resultado == 13:
        print('n')
    elif resultado == 14:
        print('o')
    elif resultado == 15:
        print('p')
    elif resultado == 16:
        print('q')
    elif resultado == 17:
        print('r')
    elif resultado == 18:
        print('s')
    elif resultado == 19:
        print('t')
    elif resultado == 20:
        print('u')
    elif resultado == 21:
        print('v')
    elif resultado == 22:
        print('w')
    elif resultado == 23:
        print('x')
    elif resultado == 24:
        print('y')
    elif resultado == 25:
        print('z')


respuesta = """
hola cambia numeros por letras
elije un numero que quieras cambiar: 

"""
numero = int(input(respuesta))

if int(numero / 26) <= 26:
    resultado = int(numero % 26)
    respuestas3()
    resultado = int((numero / 26) - 1)
    respuestas3()
elif int(numero / 26) <= 702:
    resultado = int(numero % 26)
    respuestas3()
    resultado2 = int((numero / 26) - 1)
    resultado = int(resultado2 % 26)
    respuestas3()
    resultado = int((resultado2 / 26) - 1)
    respuestas3()
elif int(numero / 26) <= 18278:
    resultado = int(numero % 26)
    respuestas3()
    resultado2 = int((numero / 26) - 1)
    resultado = int(resultado2 % 26)
    respuestas3()
    resultado3 = int((resultado2 / 26) - 1)
    resultado = int(resultado3 % 26)
    respuestas3()
    resultado = int((resultado3 / 26) - 1)
    respuestas3()
elif int(numero / 26) <= 475254:
    resultado = int(numero % 26)
    respuestas3()
    resultado2 = int((numero / 26) - 1)
    resultado = int(resultado2 % 26)
    respuestas3()
    resultado3 = int((resultado2 / 26) - 1)
    resultado = int(resultado3 % 26)
    respuestas3()
    resultado4 = int((resultado3 / 26) - 1)
    resultado = int(resultado4 / 26)
    respuestas3()
    resultado = int((resultado4 / 26) - 1)
    respuestas3()
elif int(numero / 26) <= 12356630:
    resultado = int(numero % 26)
    respuestas3()
    resultado2 = int((numero / 26) - 1)
    resultado = int(resultado2 % 26)
    respuestas3()
    resultado3 = int((resultado2 / 26) - 1)
    resultado = int(resultado3 % 26)
    respuestas3()
    resultado4 = int((resultado3 / 26) - 1)
    resultado = int(resultado4 / 26)
    respuestas3()
    resultado5 = int((resultado4 / 26) - 1)
    resultado = int(resultado5 / 26)
    respuestas3()
    resultado = int((resultado5 / 26) - 1)
    respuestas3()
elif int(numero / 26) <= 321272406:
    resultado = int(numero % 26)
    respuestas3()
    resultado2 = int((numero / 26) - 1)
    resultado = int(resultado2 % 26)
    respuestas3()
    resultado3 = int((resultado2 / 26) - 1)
    resultado = int(resultado3 % 26)
    respuestas3()
    resultado4 = int((resultado3 / 26) - 1)
    resultado = int(resultado4 / 26)
    respuestas3()
    resultado5 = int((resultado4 / 26) - 1)
    resultado = int(resultado5 / 26)
    respuestas3()
    resultado6 = int((resultado5 / 26) - 1)
    resultado = int(resultado6 / 26)
    respuestas3()
    resultado = int((resultado6 / 26) - 1)
    respuestas3()
else:
    print('numero muy grande me cree marica')