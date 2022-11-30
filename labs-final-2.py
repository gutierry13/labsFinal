valor = str(input('Qual a palavra? '))


def repetido(string):
    transformUpper = string.upper()
    quebraString = list(transformUpper)
    repetiu = 1
    for x in range(len(quebraString)):
        pop = quebraString.pop(0)
        if pop in quebraString:
            repetiu += 1
    if repetiu != 1:
        return bool(repetiu)
    else:
        return bool(repetiu - 1)


def tentativa(string):
    try:
        return repetido(string)
    except:
        print('Houve um erro na função')


print(tentativa(valor))
