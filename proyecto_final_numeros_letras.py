numero = int(input(" hola man cambia numeros por letras elije un numero que quieras cambiar: "))
cosciente = numero
def run():
    result = []
    resultado2 = numero
    cosciente = int(resultado2 % 26)
    letras_y_numeros = {}
    letras2 = 'abcdefghijklmnopqrstuvwxyz'.upper()
    for i, letras in enumerate(letras2):
        if not letras_y_numeros.get(i):
            letras_y_numeros[i] = []
        letras_y_numeros[i].append(letras)
    for i in letras_y_numeros[cosciente]:
        result.append(i)
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
            result.append(i)
    result = str(result)
    result = result[::-1]
    specialchars = "[]'' ,"
    for e in specialchars:
        result = result.replace(e, '')
    print(result)


if __name__ == '__main__':
    run()