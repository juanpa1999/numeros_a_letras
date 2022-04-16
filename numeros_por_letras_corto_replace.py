def run():
    letras_y_numeros = {}
    letras2 = 'abcdefghijklmnopqrstuvwxyz'.upper()
    for i, letras in enumerate(letras2):
        #print(i, letras)
        if not letras_y_numeros.get(i):
            letras_y_numeros[i] = []
        letras_y_numeros[i].append(letras)
    print(letras_y_numeros)
    variable = 24
    for i in letras_y_numeros[variable]:
        print(i)
    for i, e in letras_y_numeros.items():
        e = str(e)
        specialChars = "[]''"
        for specialChar in specialChars:
            e = e.replace(specialChar, '')
        if i ==25:
            print(i, '-', e)

if __name__ == '__main__':
    run()

