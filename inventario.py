import pygame

from constantes import *

class Inventario:
    def __init__(self):
        self.posiciones = []
        self.rectas = []
        self.pantalla = pygame.display.get_surface()

    def inventarios(self):
        fondo = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
        fondo.fill(COLOR_FONDO_INVENTARIO)
        self.pantalla.blit(fondo,(0,0))
        
        for fil in range(1,5):
            n = 0
            for col in range(1,8):
                pygame.draw.rect(self.pantalla,
                                 COLOR_CUADROS_INVENTARIO,
                                 (col * TAMANO_CUADROS_INVENTARIO[0] + n,
                                  fil * TAMANO_CUADROS_INVENTARIO[1] + fil* n,
                                  TAMANO_CUADROS_INVENTARIO[0],
                                  TAMANO_CUADROS_INVENTARIO[1]))
                self.posiciones.append((col * TAMANO_CUADROS_INVENTARIO[0] + n ,
                                        TAMANO_CUADROS_INVENTARIO[1] + fil* n))
                n += TAMANO_CUADROS_INVENTARIO[0]//6
        
        for cuadro in self.posiciones:
            self.rectas.append(pygame.Rect(cuadro[0],
                                           cuadro[1],
                                           TAMANO_CUADROS_INVENTARIO[0],
                                           TAMANO_CUADROS_INVENTARIO[1]))