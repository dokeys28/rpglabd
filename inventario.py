import pygame

from constantes import *


class Inventario:
    def __init__(self):
        self.posiciones = []
        self.rectas = []
        self.pantalla = pygame.display.get_surface()
        self.cuadros = dict()
        self.fondo = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
        self.fondo.fill(COLOR_FONDO_INVENTARIO)
        self.guardar()
    
    def guardar(self):
        for fil in range(1,5):
            n = 0
            for col in range(1,8):
                self.posiciones.append((col * TAMANO_CUADROS_INVENTARIO[0] + n ,
                                        fil * TAMANO_CUADROS_INVENTARIO[1] + fil* 10))
                n += TAMANO_CUADROS_INVENTARIO[0]//6
        for cuadro in self.posiciones:
            self.rectas.append(pygame.Rect(cuadro[0],
                                           cuadro[1],
                                           TAMANO_CUADROS_INVENTARIO[0],
                                           TAMANO_CUADROS_INVENTARIO[1]))
        for i, xcuadro in enumerate(self.rectas):
            self.cuadros[f'cuadro {i + 1}'] = xcuadro
            
    def actualizar(self, lista_de_items):

        self.pantalla.blit(self.fondo,(0,0))
        for fil in range(1,5):
            n = 0
            for col in range(1,8):
                pygame.draw.rect(self.pantalla,
                                 COLOR_CUADROS_INVENTARIO,
                                 (col * TAMANO_CUADROS_INVENTARIO[0] + n,
                                  fil * TAMANO_CUADROS_INVENTARIO[1] + fil* 10,
                                  TAMANO_CUADROS_INVENTARIO[0],
                                  TAMANO_CUADROS_INVENTARIO[1]))
                n += TAMANO_CUADROS_INVENTARIO[0]//6
        
        for item in lista_de_items:
            item.actualizar(self)