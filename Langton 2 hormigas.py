"""
    @author Daniel Cano
    Tomado de http://www.solveet.com/exercises/Hormiga-de-Langton/402/solution-2336
    Pasado de python2 a python3 bajo los estándares de pep8
    python Langton.py
"""

import pygame
import sys
from pygame.locals import*

pygame.init()


def dibujarM(window, matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                pygame.draw.rect(window, (0, 0, 0, 0), (j*10, i*10, 10, 10), 1)
            else:
                pygame.draw.rect(window, (0, 0, 0, 0), (j*10, i*10, 10, 10), 0)


def crearMatriz(n):

    lista = []
    for i in range(n):
        lista.append([])
        for j in range(n):
            lista[i].append(0)

    return lista


def estado(estado_, bandera):
    if bandera == "derecha":
        if estado_ == "arriba":
            return "derecha"
        elif estado_ == "derecha":
            return "abajo"
        elif estado_ == "abajo":
            return "izquierda"
        else:
            return "arriba"
    else:
        if estado_ == "arriba":
            return "izquierda"
        elif estado_ == "derecha":
            return "arriba"
        elif estado_ == "abajo":
            return "derecha"
        else:
            return "abajo"


def mover(matriz, hm1):

    if hm1[0] > (len(matriz)-1):
        hm1[0] = int(len(matriz)/2)
    if hm1[0] < 0:
        hm1[0] = int(len(matriz)/2)
    if hm1[1] > (len(matriz)-1):
        hm1[1] = int(len(matriz)/2)
    if hm1[1] < 0:
        hm1[1] = int(len(matriz)/2)

    if matriz[hm1[0]][hm1[1]] == 0:
        matriz[hm1[0]][hm1[1]] = 1
        hm1[2] = estado(hm1[2], "derecha")
        if hm1[2] == "arriba":
            hm1[0] -= 1
        elif hm1[2] == "derecha":
            hm1[1] += 1
        elif hm1[2] == "abajo":
            hm1[0] += 1
        else:
            hm1[1] -= 1
    else:
        matriz[hm1[0]][hm1[1]] = 0
        hm1[2] = estado(hm1[2], "izquierda")
        if hm1[2] == "arriba":
            hm1[0] -= 1
        elif hm1[2] == "derecha":
            hm1[1] += 1
        elif hm1[2] == "abajo":
            hm1[0] += 1
        else:
            hm1[1] -= 1
    return matriz, hm1

    pass


def start():

    window = pygame.display.set_mode((1024, 768))
    matriz = crearMatriz(100)
    posX1, posY1, estado1 = 20, 25, "arriba"
    posX2, posY2, estado2 = 25, 25, "arriba"
    hormiga1 = [posY1, posX1, estado1]
    hormiga2 = [posY2, posX2, estado2]
    
    while True:
        window.fill((230, 230, 230))
        matriz, hormiga1 = mover(matriz, hormiga1)
        matriz, hormiga2 = mover(matriz, hormiga2)
        dibujarM(window, matriz)

        for events in pygame.event.get():
            if events.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def main():
    start()
    pass


main()
