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
        self.visible = False
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
            
    def handler(self, event, lista_de_items):
        print('Probando')
        for c in self.cuadros.keys():
            if self.cuadros[c].collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
                cuadro_x_labo = c
                #mostrar descripcion del item
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            item_pisado = cuadro_x_labo

            
        if event.type == pygame.MOUSEBUTTONUP:
            item_suelto = cuadro_x_labo
            for item in lista_de_items:
                if item.cuadro == item_pisado:
                    item.cuadro = item_suelto
                item.actualizar(self)  


    def actualizar(self, evento, lista_de_items):
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
        
        if self.visible:
            self.handler(evento, lista_de_items)
