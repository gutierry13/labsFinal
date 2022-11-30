from random import random
linhas = int(input('Quantas linhas a matriz tera?'))
colunas = int(input('Quantas colunas a matriz tera?'))


def separarParesEImpar(array):
    matrizPar = []
    matrizImpar = []
    novaMatrizFinal = []
    for i in array:
        if i % 2 == 0:
            matrizPar.append(i)
        else:
            matrizImpar.append(i)
        matrizPar.sort()
        matrizImpar.sort()
    novaMatrizFinal.extend(matrizPar)
    novaMatrizFinal.extend(matrizImpar)
    print(novaMatrizFinal)


def organizarMatriz(array):
    matrizFinal = []
    for item in array:
        matrizFinal.extend(item)
    separarParesEImpar(matrizFinal)


def gerarMatriz(linhas, colunas):
    matriz = []
    for a in range(linhas):
        matriz.append([])
    for y in range(colunas):
        for z in range(linhas):
            matriz[z].append(completarMatriz())
    for i in matriz:
        print(i)
    organizarMatriz(matriz)


def completarMatriz():
    valor1 = round(random() * 10)
    return valor1


gerarMatriz(linhas, colunas)
