respuesta = " hola man cambia numeros por letras elije un numero que quieras cambiar: "
numero = int(input(respuesta))
cosciente = numero
def run():
    resultado2 = numero
    cosciente = int(resultado2 % 26)
    letras_y_numeros = {}
    letras2 = 'abcdefghijklmnopqrstuvwxyz'.upper()
    for i, letras in enumerate(letras2):
        if not letras_y_numeros.get(i):
            letras_y_numeros[i] = []
        letras_y_numeros[i].append(letras)
    for i in letras_y_numeros[cosciente]:
        print(i)
        return(i)
    while resultado2 > 27:
        resultado2 = int(resultado2 / 26 - 1)
        cosciente = int(resultado2 % 26)
        letras_y_numeros = {}
        letras2 = 'abcdefghijklmnopqrstuvwxyz'.upper()
        for i, letras in enumerate(letras2):
            if not letras_y_numeros.get(i):
                letras_y_numeros[i] = []
            letras_y_numeros[i].append(letras)
        for i in letras_y_numeros[cosciente]:
            print(i)
            return(i)
        


if __name__ == '__main__':
    run()