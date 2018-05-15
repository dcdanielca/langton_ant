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
                pygame.draw.rect(window, (0, 0, 0, 0), (j*5, i*5, 5, 5), 1)
            else:
                pygame.draw.rect(window, (0, 0, 0, 0), (j*5, i*5, 5, 5), 0)


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


def mover(matriz, hm):

    if hm[0] > (len(matriz)-1):
        hm[0] = int(len(matriz)/2)
    if hm[0] < 0:
        hm[0] = int(len(matriz)/2)
    if hm[1] > (len(matriz)-1):
        hm[1] = int(len(matriz)/2)
    if hm[1] < 0:
        hm[1] = int(len(matriz)/2)

    if matriz[hm[0]][hm[1]] == 0:
        matriz[hm[0]][hm[1]] = 1
        hm[2] = estado(hm[2], "derecha")
        if hm[2] == "arriba":
            hm[0] -= 1
        elif hm[2] == "derecha":
            hm[1] += 1
        elif hm[2] == "abajo":
            hm[0] += 1
        else:
            hm[1] -= 1
    else:
        matriz[hm[0]][hm[1]] = 0
        hm[2] = estado(hm[2], "izquierda")
        if hm[2] == "arriba":
            hm[0] -= 1
        elif hm[2] == "derecha":
            hm[1] += 1
        elif hm[2] == "abajo":
            hm[0] += 1
        else:
            hm[1] -= 1
    return matriz, hm

    pass


def start():

    window = pygame.display.set_mode((1366, 768))
    matriz = crearMatriz(300)
    posX, posY, estado = 150, 30, "arriba"
    hormiga = [posY, posX, estado]
    
    clock = pygame.time.Clock()
    clock.tick(1000)
    count = 0  # count contiene el número de iteraciones  

    window.fill((230, 230, 230))
    while True:
        matriz, hormiga = mover(matriz, hormiga)
        if count > 372500:
            dibujarM(window, matriz)
            pygame.display.update()

        for events in pygame.event.get():
            if events.type == QUIT:
                pygame.quit()
                sys.exit()

        count +=1


def main():
    start()
    pass


main()
